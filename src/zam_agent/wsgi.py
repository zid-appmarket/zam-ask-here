"""Production WSGI entry point.

    gunicorn --workers 1 --threads 8 --bind 0.0.0.0:3000 zam_agent.wsgi:application

Use a **single worker process** with threads: event de-duplication is durable
(SQLite), but one process keeps the knowledge index in one place and avoids
N copies of it in memory. Scale with threads, or move the store to a shared
database before scaling out processes.
"""

from __future__ import annotations

from .runtime import build_runtime, build_wsgi_app

runtime = build_runtime()
application = build_wsgi_app(runtime)
