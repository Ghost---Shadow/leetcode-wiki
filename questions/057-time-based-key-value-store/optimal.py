import bisect


class TimeMap:
    """Optimal TimeMap: appends are already in increasing timestamp order
    (per LeetCode's guarantee), so each key's list stays sorted by
    timestamp. get() binary-searches for the largest timestamp <= query,
    O(log n) per get instead of a linear scan."""

    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        self.store.setdefault(key, []).append((timestamp, value))

    def get(self, key, timestamp):
        entries = self.store.get(key)
        if not entries:
            return ""
        idx = bisect.bisect_right(entries, (timestamp, chr(0x10FFFF)))
        if idx == 0:
            return ""
        return entries[idx - 1][1]


def solve(operations, arguments):
    """Replays a LeetCode-style operation log against TimeMap.

    operations[0] is always "TimeMap" (the constructor call).
    Returns a list of results, one per operation (None for void calls).
    """
    results = []
    obj = None
    for op, args in zip(operations, arguments):
        if op == "TimeMap":
            obj = TimeMap(*args)
            results.append(None)
        elif op == "set":
            obj.set(*args)
            results.append(None)
        elif op == "get":
            results.append(obj.get(*args))
        else:
            raise ValueError(f"Unknown operation: {op}")
    return results
