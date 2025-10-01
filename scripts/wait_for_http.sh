#!/usr/bin/env bash
set -euo pipefail

URL="$1"         # e.g., http://localhost:5001/health
TIMEOUT="${2:-120}"  # seconds

echo "[wait_for_http] Waiting for $URL (timeout ${TIMEOUT}s)"
start=$(date +%s)
while true; do
  if curl -fsS "$URL" >/dev/null 2>&1; then
    echo "[wait_for_http] OK: $URL is up"
    exit 0
  fi
  now=$(date +%s)
  elapsed=$(( now - start ))
  if [ "$elapsed" -ge "$TIMEOUT" ]; then
    echo "[wait_for_http] ERROR: timeout after ${TIMEOUT}s waiting for $URL" >&2
    exit 1
  fi
  sleep 2
done