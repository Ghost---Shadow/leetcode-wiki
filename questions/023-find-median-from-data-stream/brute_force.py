class MedianFinder:
    """Brute-force: keep every number in a plain list and re-sort it from
    scratch on every findMedian() call, instead of maintaining two heaps."""

    def __init__(self):
        self.nums = []

    def addNum(self, num):
        self.nums.append(num)

    def findMedian(self):
        nums = sorted(self.nums)
        n = len(nums)
        mid = n // 2
        if n % 2 == 1:
            return float(nums[mid])
        return (nums[mid - 1] + nums[mid]) / 2.0


def solve(operations, arguments):
    """Replays a LeetCode-style operation log against MedianFinder.

    operations[0] is always "MedianFinder" (the constructor call).
    Returns a list of results, one per operation (None for void calls).
    """
    results = []
    obj = None
    for op, args in zip(operations, arguments):
        if op == "MedianFinder":
            obj = MedianFinder()
            results.append(None)
        elif op == "addNum":
            obj.addNum(*args)
            results.append(None)
        elif op == "findMedian":
            results.append(obj.findMedian())
        else:
            raise ValueError(f"Unknown operation: {op}")
    return results
