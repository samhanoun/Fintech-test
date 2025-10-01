#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   deploy_blue_green_local.sh TARGET=uat|prod MODE=image|build IMAGE_NAME=ghcr.io/org/repo/bank-api IMAGE_TAG=<tag>
# Example:
#   deploy_blue_green_local.sh TARGET=uat MODE=build IMAGE_TAG=$(git rev-parse --short HEAD)
#   deploy_blue_green_local.sh TARGET=prod MODE=image IMAGE_NAME=ghcr.io/org/repo/bank-api IMAGE_TAG=v1.2.3

# Parse KEY=VALUE args
for arg in "$@"; do
  case $arg in
    TARGET=*) TARGET="${arg#*=}" ;;
    MODE=*) MODE="${arg#*=}" ;;
    IMAGE_NAME=*) IMAGE_NAME="${arg#*=}" ;;
    IMAGE_TAG=*) IMAGE_TAG="${arg#*=}" ;;
    RUN_SMOKE=*) RUN_SMOKE="${arg#*=}" ;;
    *) echo "Unknown arg: $arg" ;;
  esac
done

TARGET=${TARGET:-uat}
MODE=${MODE:-image}         # image (pull) or build (local)
IMAGE_NAME=${IMAGE_NAME:-ghcr.io/example-org/fintech-test/bank-api}
IMAGE_TAG=${IMAGE_TAG:-latest}
RUN_SMOKE=${RUN_SMOKE:-true}

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

if [[ "$TARGET" == "uat" ]]; then
  COMPOSE_FILE="docker/docker-compose.uat.yml"
  HEALTH_URL="http://localhost:5001/health"
  # UAT is single instance, no blue/green switch
  echo "[deploy] UAT deployment starting (MODE=$MODE, IMAGE=$IMAGE_NAME:$IMAGE_TAG)"
  if [[ "$MODE" == "image" ]]; then
    IMAGE_NAME="$IMAGE_NAME" IMAGE_TAG="$IMAGE_TAG" docker compose -f "$COMPOSE_FILE" pull --quiet || true
  fi
  IMAGE_NAME="$IMAGE_NAME" IMAGE_TAG="$IMAGE_TAG" docker compose -f "$COMPOSE_FILE" up -d --build
  bash scripts/wait_for_http.sh "$HEALTH_URL" 180
  if [[ "$RUN_SMOKE" == "true" ]]; then
    echo "[deploy] Running k6 smoke against $HEALTH_URL"
    BASE_URL="http://host.docker.internal:5001"
    docker run --rm --add-host=host.docker.internal:host-gateway -e BASE_URL="$BASE_URL" -v "$ROOT_DIR/k6:/scripts" grafana/k6:0.51.0 run /scripts/perf-smoke.js
  fi
  echo "[deploy] UAT deployed. Show status and logs:"
  docker compose -f "$COMPOSE_FILE" ps
  docker compose -f "$COMPOSE_FILE" logs --tail=200 api || true
  exit 0
fi

if [[ "$TARGET" == "prod" ]]; then
  COMPOSE_FILE="docker/docker-compose.prod.yml"
  ACTIVE_SLOT_FILE=".active_slot"
  HEALTH_URL="http://localhost:5002/health"
  ACTIVE="blue"
  if [[ -f "$ACTIVE_SLOT_FILE" ]]; then
    ACTIVE="$(cat "$ACTIVE_SLOT_FILE")"
  fi
  INACTIVE="green"; [[ "$ACTIVE" == "green" ]] && INACTIVE="blue"
  echo "[deploy] PROD blue/green current active=$ACTIVE, will deploy to $INACTIVE"

  # Bring up DB if not running
  docker compose -f "$COMPOSE_FILE" up -d db

  # Deploy inactive slot
  if [[ "$MODE" == "image" ]]; then
    IMAGE_NAME="$IMAGE_NAME" IMAGE_TAG="$IMAGE_TAG" docker compose -f "$COMPOSE_FILE" --profile "$INACTIVE" pull --quiet || true
  fi
  IMAGE_NAME="$IMAGE_NAME" IMAGE_TAG="$IMAGE_TAG" docker compose -f "$COMPOSE_FILE" --profile "$INACTIVE" up -d --build

  # Healthcheck inactive slot internally (no host port). Use container exec via service name.
  echo "[deploy] Waiting for $INACTIVE service health"
  tries=0
  until docker compose -f "$COMPOSE_FILE" ps "api_$INACTIVE" | grep -q "healthy"; do
    sleep 3; tries=$((tries+1)); if [[ $tries -gt 60 ]]; then echo "[deploy] ERROR: $INACTIVE not healthy"; exit 1; fi
  done

  # Switch traffic: stop active (which exposes host port 5002), start inactive with port mapping
  echo "[deploy] Switching traffic from $ACTIVE to $INACTIVE"
  docker compose -f "$COMPOSE_FILE" --profile "$ACTIVE" stop "api_$ACTIVE" || true
  # Recreate inactive with port mapping by toggling profiles: stop inactive, then start as active profile
  docker compose -f "$COMPOSE_FILE" --profile "$INACTIVE" stop "api_$INACTIVE" || true
  # Now bring up the new active (will publish 5002 when profile is blue)
  NEW_ACTIVE="$INACTIVE"; NEW_INACTIVE="$ACTIVE"
  if [[ "$NEW_ACTIVE" == "blue" ]]; then
    docker compose -f "$COMPOSE_FILE" --profile blue up -d
  else
    # Temporarily map 5002 for green by running a one-off publish using docker run
    # Simpler approach: re-use blue profile but with the new image tag (flip active slot file)
    docker compose -f "$COMPOSE_FILE" --profile green up -d
  fi

  # Wait external health
  bash scripts/wait_for_http.sh "$HEALTH_URL" 180

  if [[ "$RUN_SMOKE" == "true" ]]; then
    echo "[deploy] Running k6 smoke against $HEALTH_URL"
    BASE_URL="http://host.docker.internal:5002"
    docker run --rm --add-host=host.docker.internal:host-gateway -e BASE_URL="$BASE_URL" -v "$ROOT_DIR/k6:/scripts" grafana/k6:0.51.0 run /scripts/perf-smoke.js
  fi

  echo "$NEW_ACTIVE" > "$ACTIVE_SLOT_FILE"
  echo "[deploy] PROD switched. Active now: $NEW_ACTIVE"
  docker compose -f "$COMPOSE_FILE" ps
  docker compose -f "$COMPOSE_FILE" logs --tail=200 "api_$NEW_ACTIVE" || true
  exit 0
fi

echo "[deploy] Unknown TARGET=$TARGET (expected uat or prod)" >&2
exit 2
