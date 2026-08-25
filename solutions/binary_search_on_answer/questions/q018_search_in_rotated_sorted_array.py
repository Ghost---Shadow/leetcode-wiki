"""Reshaper for questions/q018_search_in_rotated_sorted_array.

Converts this question's (nums, target) -> int I/O into a call to the
shared binary_search_converge(): state = (left, right, found), where
`found` starts at -1 and gets set the moment target is located; once set,
the next step call sees found != -1 and reports the state as terminal.
"""
from .. import algorithm as _algorithm
binary_search_converge = _algorithm.binary_search_converge


def solve(nums, target):
    def step(state):
        left, right, found = state
        if found != -1 or left > right:
            return None
        mid = (left + right) // 2
        if nums[mid] == target:
            return (left, right, mid)
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                return (left, mid - 1, -1)
            return (mid + 1, right, -1)
        else:
            if nums[mid] < target <= nums[right]:
                return (mid + 1, right, -1)
            return (left, mid - 1, -1)

    _, _, found = binary_search_converge((0, len(nums) - 1, -1), step)
    return found
