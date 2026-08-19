from collections import deque


class HitCounter:
    """Optimal: store hit timestamps in a deque (they arrive in
    non-decreasing order per LeetCode's constraints), evicting expired
    timestamps from the front on every call. Each timestamp is pushed and
    popped at most once, giving amortized O(1) time per hit()/getHits()
    call instead of the brute force's O(n) full rescan per getHits()."""

    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp):
        self.hits.append(timestamp)

    def getHits(self, timestamp):
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        return len(self.hits)


def solve(operations, arguments):
    """Replays a LeetCode-style operation log against HitCounter.

    operations[0] is always "HitCounter" (the constructor call).
    Returns a list of results, one per operation (None for void methods).
    """
    results = []
    obj = None
    for op, args in zip(operations, arguments):
        if op == "HitCounter":
            obj = HitCounter(*args)
            results.append(None)
        elif op == "hit":
            obj.hit(*args)
            results.append(None)
        elif op == "getHits":
            results.append(obj.getHits(*args))
        else:
            raise ValueError(f"Unknown operation: {op}")
    return results
