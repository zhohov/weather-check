DC := docker-compose
TEST_DC := docker-compose.test.yaml
DEV_DC := docker-compose.dev.yaml
env ?= test

ifeq ($(env),test)
    CURRENT_DC := $(TEST_DC)
else ifeq ($(env),dev)
	CURRENT_DC := $(DEV_DC)
else
    $(error Invalid value for env: $(env). Valid values are 'test' or 'dev'.)
endif

.PHONY: up
up:
	$(DC) -f $(CURRENT_DC) up

.PHONY: build
build:
	$(DC) -f $(CURRENT_DC) up --build

.PHONY: export
export:
	cd backend && poetry export --without-hashes --format=requirements.txt > requirements.txt

