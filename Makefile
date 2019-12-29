DOCKER_REGISTRY := 
DOCKER_VERSION := $(shell git rev-parse --short HEAD)
APPS := kubeweekly_telegram_bot

.PHONY: build
build: 
	docker build -t $(DOCKER_REGISTRY)/$(APPS):$(DOCKER_VERSION) .

.PHONY: push
push:
	docker push $(DOCKER_REGISTRY)/$(APPS):$(DOCKER_VERSION)
