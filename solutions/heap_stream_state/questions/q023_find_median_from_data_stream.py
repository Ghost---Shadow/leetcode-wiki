"""Reshaper for questions/q023_find_median_from_data_stream.

Converts this question's LeetCode-judge replay format (operations,
arguments) -> list I/O into a call to the shared TwoHeapMedian: replays
each operation against a fresh instance, appending None for void calls.
"""
from .. import algorithm as _algorithm
TwoHeapMedian = _algorithm.TwoHeapMedian


def solve(operations, arguments):
    results = []
    obj = None
    for op, args in zip(operations, arguments):
        if op == "MedianFinder":
            obj = TwoHeapMedian()
            results.append(None)
        elif op == "addNum":
            obj.push(*args)
            results.append(None)
        elif op == "findMedian":
            results.append(obj.median())
        else:
            raise ValueError(f"Unknown operation: {op}")
    return results
