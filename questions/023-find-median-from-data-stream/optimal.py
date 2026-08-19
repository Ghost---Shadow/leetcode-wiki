import heapq


class MedianFinder:
    """Two heaps: a max-heap (negated) for the lower half of numbers and a
    min-heap for the upper half, kept balanced in size. addNum is
    O(log n), findMedian is O(1), instead of re-sorting on every call."""

    def __init__(self):
        self.lo = []  # max-heap (store negated values)
        self.hi = []  # min-heap

    def addNum(self, num):
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))

        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return float(-self.lo[0])
        return (-self.lo[0] + self.hi[0]) / 2.0


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
