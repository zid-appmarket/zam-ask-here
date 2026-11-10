# syntax=docker/dockerfile:1
FROM python:3.12-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Dependencies first so the layer caches across code changes.
COPY pyproject.toml README.md ./
COPY src/ ./src/
RUN pip install --no-cache-dir .

COPY scripts/ ./scripts/
COPY knowledge/ ./knowledge/

# The SQLite database holds event de-duplication and escalation state, so it
# MUST outlive the container. Mount a volume here.
RUN mkdir -p /data && chown -R 1000:1000 /data /app
VOLUME ["/data"]
ENV DATABASE_URL=sqlite:////data/zam_agent.db \
    KNOWLEDGE_SNAPSHOT_PATH=/data/knowledge_index.json \
    KNOWLEDGE_DIR=/app/knowledge

USER 1000:1000

# Fails while the knowledge base is empty, which is the right signal: an agent
# with no sources can only escalate.
HEALTHCHECK --interval=60s --timeout=15s --start-period=30s --retries=3 \
    CMD ["python", "-m", "zam_agent", "--health"]

# Socket Mode by default: no inbound port required.
CMD ["python", "-m", "zam_agent"]
