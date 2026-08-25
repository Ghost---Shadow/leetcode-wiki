"""Reshaper for questions/q064_find_first_and_last_position_of_element_in_sorted_array.

Converts this question's (nums, target) -> list[int] I/O into two calls to
the shared binary_search_converge(): a bisect_left-style search and a
bisect_right-style search, each with state = (lo, hi) converging to a
single boundary index.
"""
from .. import algorithm as _algorithm
binary_search_converge = _algorithm.binary_search_converge


def _bisect_left(nums, target):
    def step(state):
        lo, hi = state
        if lo >= hi:
            return None
        mid = (lo + hi) // 2
        if nums[mid] < target:
            return (mid + 1, hi)
        return (lo, mid)

    lo, _ = binary_search_converge((0, len(nums)), step)
    return lo


def _bisect_right(nums, target):
    def step(state):
        lo, hi = state
        if lo >= hi:
            return None
        mid = (lo + hi) // 2
        if nums[mid] <= target:
            return (mid + 1, hi)
        return (lo, mid)

    lo, _ = binary_search_converge((0, len(nums)), step)
    return lo


def solve(nums, target):
    left = _bisect_left(nums, target)
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    right = _bisect_right(nums, target) - 1
    return [left, right]
