from collections import defaultdict
from collections.abc import Iterable, Mapping


def summarize_flows(flows: Iterable[Mapping[str, object]]) -> list[dict[str, object]]:
    """Aggregate flow records by protocol and endpoint pair.

    Expected fields are protocol, source, destination, and bytes. Missing byte
    counts are treated as zero. Input records are never modified.
    """
    totals: dict[tuple[str, str, str], int] = defaultdict(int)
    for flow in flows:
        protocol = str(flow.get("protocol", "unknown"))
        source = str(flow.get("source", "unknown"))
        destination = str(flow.get("destination", "unknown"))
        value = flow.get("bytes", 0)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("bytes must be numeric")
        if value < 0:
            raise ValueError("bytes cannot be negative")
        totals[(protocol, source, destination)] += int(value)

    return [
        {
            "protocol": protocol,
            "source": source,
            "destination": destination,
            "bytes": total,
        }
        for (protocol, source, destination), total in sorted(totals.items())
    ]
