import random


class RandomizedSet:
    """Optimal: store elements in a list (for O(1) uniform random access)
    plus a hash map from value -> index in that list. Insert appends;
    remove swaps the target with the last element (updating the map) then
    pops, avoiding a costly middle-of-list shift. All operations are O(1)
    average time, O(n) space."""

    def __init__(self):
        self.data = []
        self.index = {}

    def insert(self, val):
        if val in self.index:
            return False
        self.index[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val):
        if val not in self.index:
            return False
        idx = self.index[val]
        last_val = self.data[-1]
        self.data[idx] = last_val
        self.index[last_val] = idx
        self.data.pop()
        del self.index[val]
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
