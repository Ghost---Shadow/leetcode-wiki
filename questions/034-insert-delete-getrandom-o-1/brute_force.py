import random


class RandomizedSet:
    """Brute-force: uses a plain list for storage, so insert/remove/contains
    are all O(n) linear scans instead of O(1) with a value-to-index hash map."""

    def __init__(self):
        self.data = []

    def insert(self, val):
        if val in self.data:
            return False
        self.data.append(val)
        return True

    def remove(self, val):
        if val not in self.data:
            return False
        self.data.remove(val)
        return True

    def getRandom(self):
        return random.choice(self.data)


def solve(operations, arguments):
    """Replays a LeetCode-style operation log against RandomizedSet.

    operations[0] is always "RandomizedSet" (the constructor call).
    Returns a list of results, one per operation (None for void calls).
    """
    results = []
    obj = None
    for op, args in zip(operations, arguments):
        if op == "RandomizedSet":
            obj = RandomizedSet()
            results.append(None)
        elif op == "insert":
            results.append(obj.insert(*args))
        elif op == "remove":
            results.append(obj.remove(*args))
        elif op == "getRandom":
            results.append(obj.getRandom())
        else:
            raise ValueError(f"Unknown operation: {op}")
    return results
