"""Minimal in-process counters, exposed on the health endpoint.

Deliberately dependency-free: swap for Prometheus/StatsD by reimplementing
``Metrics`` -- the rest of the codebase only calls ``incr`` / ``observe``.
"""

from __future__ import annotations

import threading
from collections import Counter, defaultdict
from typing import Any


class Metrics:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._counters: Counter[str] = Counter()
        self._observations: dict[str, list[float]] = defaultdict(list)

    def incr(self, name: str, value: int = 1) -> None:
        with self._lock:
            self._counters[name] += value

    def observe(self, name: str, value: float) -> None:
        with self._lock:
            series = self._observations[name]
            series.append(value)
            if len(series) > 1000:
                del series[:-1000]

    def snapshot(self) -> dict[str, Any]:
        with self._lock:
            counters = dict(self._counters)
            summaries = {
                name: {
                    "count": len(values),
                    "avg": round(sum(values) / len(values), 4),
                    "max": round(max(values), 4),
                }
                for name, values in self._observations.items()
                if values
            }
        return {"counters": counters, "timings": summaries}


METRICS = Metrics()
