# Socket Mode (recommended): one process, no inbound URL, no load balancer.
worker: python -m zam_agent

# HTTP Events API alternative. Use ONE worker process with threads: the
# knowledge index is in-process, and a single writer keeps SQLite simple.
web: gunicorn --workers 1 --threads 8 --timeout 120 --bind 0.0.0.0:$PORT zam_agent.wsgi:application
