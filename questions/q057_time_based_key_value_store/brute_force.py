class TimeMap:
    """Brute-force TimeMap: stores every (timestamp, value) pair per key and
    does a full linear scan to find the best timestamp <= the query, instead
    of appending in sorted order and binary-searching."""

    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        self.store.setdefault(key, []).append((timestamp, value))

    def get(self, key, timestamp):
        best_ts = -1
        best_val = ""
        for ts, val in self.store.get(key, []):
            if ts <= timestamp and ts > best_ts:
                best_ts = ts
                best_val = val
        return best_val


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
