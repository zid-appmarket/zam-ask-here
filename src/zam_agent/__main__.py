"""Entry point: ``python -m zam_agent``.

Socket Mode (default) needs no public URL and is the easiest way to run the
agent. ``SLACK_MODE=http`` serves the Events API over HTTP; for production use
a real WSGI server against ``zam_agent.wsgi:application`` rather than the
development server started here.
"""

from __future__ import annotations

import contextlib
import signal
import sys
from types import FrameType

from .config import ConfigError, load_config
from .observability.logging import configure_logging, get_logger
from .runtime import build_runtime, build_wsgi_app, run_socket_mode

log = get_logger(__name__)


def main(argv: list[str] | None = None) -> int:
    argv = list(argv if argv is not None else sys.argv[1:])
    try:
        config = load_config()
    except ConfigError as exc:
        configure_logging("INFO", "text")
        log.error("configuration error: %s", exc)
        return 2

    runtime = build_runtime(config)

    def _shutdown(signum: int, _frame: FrameType | None) -> None:
        log.info("shutting down", extra={"context": {"signal": signum}})
        runtime.agent.shutdown(wait=True)
        sys.exit(0)

    for sig in (signal.SIGINT, signal.SIGTERM):
        # Signals can only be installed on the main thread.
        with contextlib.suppress(ValueError):  # pragma: no cover
            signal.signal(sig, _shutdown)

    if "--health" in argv:
        import json

        print(json.dumps(runtime.agent.health(), indent=2, ensure_ascii=False, default=str))
        return 0

    if config.slack.mode == "socket":
        run_socket_mode(runtime)
        return 0

    from wsgiref.simple_server import make_server

    application = build_wsgi_app(runtime)
    log.warning(
        "serving the Events API with the development WSGI server; "
        "use gunicorn with zam_agent.wsgi:application in production"
    )
    with make_server("0.0.0.0", config.slack.port, application) as httpd:  # noqa: S104
        log.info("listening", extra={"context": {"port": config.slack.port, "path": "/slack/events"}})
        httpd.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
