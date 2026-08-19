class LFUCache:
    """Brute-force LFU: O(n) get/put via linear scan for the min-frequency (then
    least-recently-used) key, instead of the O(1) frequency-bucketed
    doubly-linked-list approach."""

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> [value, freq, last_used_tick]
        self.tick = 0

    def get(self, key):
        self.tick += 1
        if key not in self.cache:
            return -1
        self.cache[key][1] += 1
        self.cache[key][2] = self.tick
        return self.cache[key][0]

    def put(self, key, value):
        if self.capacity <= 0:
            return
        self.tick += 1
        if key in self.cache:
            self.cache[key][0] = value
            self.cache[key][1] += 1
            self.cache[key][2] = self.tick
            return
        if len(self.cache) >= self.capacity:
            evict_key = min(self.cache, key=lambda k: (self.cache[k][1], self.cache[k][2]))
            del self.cache[evict_key]
        self.cache[key] = [value, 1, self.tick]


def solve(operations, arguments):
    """Replays a LeetCode-style operation log against LFUCache.

    operations[0] is always "LFUCache" (the constructor call).
    Returns a list of results, one per operation (None for void calls).
    """
    results = []
    obj = None
    for op, args in zip(operations, arguments):
        if op == "LFUCache":
            obj = LFUCache(*args)
            results.append(None)
        elif op == "get":
            results.append(obj.get(*args))
        elif op == "put":
            obj.put(*args)
            results.append(None)
        else:
            raise ValueError(f"Unknown operation: {op}")
    return results
