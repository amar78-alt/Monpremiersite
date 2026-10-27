"""Orchestre les tests et calcule les métriques QoS."""
from datetime import datetime, timezone
import math
from statistics import mean
from atelier2.tester.tests import run_tests
from atelier2.storage import save_run


def percentile95(values):
    if not values:
        return None
    values = sorted(values)
    if len(values) == 1:
        return round(values[0], 2)
    position = .95 * (len(values) - 1)
    low, high = math.floor(position), math.ceil(position)
    if low == high:
        return round(values[low], 2)
    fraction = position - low
    return round(values[low] + (values[high] - values[low]) * fraction, 2)


def run_and_store():
    results = run_tests()
    passed = sum(item["status"] == "PASS" for item in results)
    failed = len(results) - passed
    latencies = [item["latency_ms"] for item in results if isinstance(item.get("latency_ms"), (int, float))]
    total = len(results)
    summary = {
        "passed": passed, "failed": failed, "total": total,
        "error_rate": round(failed / total, 4) if total else 0,
        "availability": round(passed / total * 100, 2) if total else 0,
        "latency_avg": round(mean(latencies), 2) if latencies else None,
        "latency_p95": percentile95(latencies),
    }
    timestamp = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    run_id = save_run(timestamp, summary, results)
    return {"id": run_id, "timestamp": timestamp, "api": "Frankfurter", "summary": summary, "tests": results}
