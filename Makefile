.PHONY: help install dev test lint typecheck check ingest validate gaps simulate sync sync-check run docker-build docker-up clean

PY ?= .venv/bin/python
PIP ?= .venv/bin/pip

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}'

.venv:
	python3 -m venv .venv

install: .venv ## Install the package
	$(PIP) install -q --upgrade pip && $(PIP) install -q .

dev: .venv ## Install with dev extras
	$(PIP) install -q --upgrade pip && $(PIP) install -q -e '.[dev]'

test: ## Run the test suite
	$(PY) -m pytest

lint: ## Lint
	$(PY) -m ruff check src tests scripts

typecheck: ## Type-check
	$(PY) -m mypy

check: lint typecheck test ## Everything CI runs

validate: ## Fail if any knowledge document is malformed
	$(PY) scripts/ingest.py --validate --list

ingest: ## Rebuild the index and write an audit snapshot
	$(PY) scripts/ingest.py

sync: ## Sync the Zid help centres into knowledge/ (review the diff after)
	$(PY) scripts/sync_docs.py

sync-check: ## Show what changed upstream, without writing
	$(PY) scripts/sync_docs.py --dry-run --quiet

gaps: ## Show questions the agent could not answer
	$(PY) scripts/report_gaps.py

simulate: ## Run one question through the real pipeline: make simulate Q="..."
	$(PY) scripts/simulate.py "$(Q)"

run: ## Start the agent
	$(PY) -m zam_agent

docker-build: ## Build the container image
	docker build -t zam-ask-here:local .

docker-up: ## Run via docker compose
	docker compose up --build

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache data/knowledge_index.json
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
