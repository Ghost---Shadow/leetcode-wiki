import random


class Solution:
    """Brute-force: on every pickIndex() call, linearly scan the prefix-sum
    array to find where the random target lands, O(n) per call, instead of
    binary-searching the prefix sums in O(log n) per call."""

    def __init__(self, w):
        self.prefix = []
        total = 0
        for x in w:
            total += x
            self.prefix.append(total)
        self.total = total

    def pickIndex(self):
        target = random.randint(1, self.total)
        for i, p in enumerate(self.prefix):
            if target <= p:
                return i
        return len(self.prefix) - 1


def solve(operations, arguments):
    """Replays a LeetCode-style operation log against Solution.

    operations[0] is always "Solution" (the constructor call).
    Returns a list of results, one per operation (None for the constructor).
    """
    results = []
    obj = None
    for op, args in zip(operations, arguments):
        if op == "Solution":
            obj = Solution(*args)
            results.append(None)
        elif op == "pickIndex":
            results.append(obj.pickIndex(*args))
        else:
            raise ValueError(f"Unknown operation: {op}")
    return results
