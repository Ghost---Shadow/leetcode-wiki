"""Reshaper for questions/q059_find_peak_element.

Converts this question's (nums,) -> int I/O into a call to the shared
binary_search_converge(): state = (lo, hi), narrowing toward a peak by
always moving into the half with an ascending neighbor.
"""
from .. import algorithm as _algorithm
binary_search_converge = _algorithm.binary_search_converge


def solve(nums):
    def step(state):
        lo, hi = state
        if lo >= hi:
            return None
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            return (mid + 1, hi)
        return (lo, mid)

    lo, _ = binary_search_converge((0, len(nums) - 1), step)
    return lo
