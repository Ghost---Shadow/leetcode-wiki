class LRUCache:
    """Brute-force LRU: O(n) put/get via linear scan for the least-recently-used key,
    instead of the O(1) doubly-linked-list + hash map approach."""

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> [value, last_used_tick]
        self.tick = 0

    def get(self, key):
        self.tick += 1
        if key not in self.cache:
            return -1
        self.cache[key][1] = self.tick
        return self.cache[key][0]

    def put(self, key, value):
        self.tick += 1
        if key not in self.cache and len(self.cache) >= self.capacity:
            lru_key = min(self.cache, key=lambda k: self.cache[k][1])
            del self.cache[lru_key]
        self.cache[key] = [value, self.tick]


def solve(operations, arguments):
    """Replays a LeetCode-style operation log against LRUCache.

    operations[0] is always "LRUCache" (the constructor call).
    Returns a list of results, one per operation (None for void calls).
    """
    results = []
    obj = None
    for op, args in zip(operations, arguments):
        if op == "LRUCache":
            obj = LRUCache(*args)
            results.append(None)
        elif op == "get":
            results.append(obj.get(*args))
        elif op == "put":
            obj.put(*args)
            results.append(None)
        else:
            raise ValueError(f"Unknown operation: {op}")
    return results
