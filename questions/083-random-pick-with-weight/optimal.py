import bisect
import random


class Solution:
    """Optimal: build a prefix-sum array once at construction time, then
    binary-search it on every pickIndex() call to find where the random
    target lands. O(n) construction, O(log n) per pick instead of the
    brute force's O(n) linear scan per pick."""

    def __init__(self, w):
        self.prefix = []
        total = 0
        for x in w:
            total += x
            self.prefix.append(total)
        self.total = total

    def pickIndex(self):
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, target)


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
