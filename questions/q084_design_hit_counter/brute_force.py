class HitCounter:
    """Brute-force: store every hit's timestamp in a plain list and, on
    every getHits() call, rescan the entire list to count timestamps within
    the trailing 300-second window. O(n) per getHits() call with unbounded
    memory growth, instead of trimming a queue/deque as time advances."""

    def __init__(self):
        self.hits = []

    def hit(self, timestamp):
        self.hits.append(timestamp)

    def getHits(self, timestamp):
        return sum(1 for t in self.hits if timestamp - 300 < t <= timestamp)


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
