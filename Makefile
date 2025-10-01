# Makefile helpers for local CD

MODE ?= image
TAG ?= staging
IMAGE_NAME ?= ghcr.io/example-org/fintech-test/bank-api

.PHONY: uat-up prod-up logs-uat logs-prod switch rollback

uat-up:
	@echo "Deploy UAT (MODE=$(MODE), TAG=$(TAG))"
	bash scripts/deploy_blue_green_local.sh TARGET=uat MODE=$(MODE) IMAGE_NAME=$(IMAGE_NAME) IMAGE_TAG=$(TAG)

prod-up:
	@echo "Deploy PROD (blue/green) (MODE=$(MODE), TAG=$(TAG))"
	bash scripts/deploy_blue_green_local.sh TARGET=prod MODE=$(MODE) IMAGE_NAME=$(IMAGE_NAME) IMAGE_TAG=$(TAG)

logs-uat:
	docker compose -f docker/docker-compose.uat.yml ps
	docker compose -f docker/docker-compose.uat.yml logs --tail=200 api

logs-prod:
	docker compose -f docker/docker-compose.prod.yml ps
	docker compose -f docker/docker-compose.prod.yml logs --tail=200 api_blue || true
	docker compose -f docker/docker-compose.prod.yml logs --tail=200 api_green || true

rollback:
	@echo "Rollback $(TARGET) to tag $(TAG)"
	bash scripts/deploy_blue_green_local.sh TARGET=$(TARGET) MODE=image IMAGE_TAG=$(TAG)
