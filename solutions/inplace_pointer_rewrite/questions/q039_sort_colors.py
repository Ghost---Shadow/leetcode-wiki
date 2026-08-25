"""Reshaper for questions/q039_sort_colors.

Converts this question's (nums,) -> list[int] I/O into a call to the
shared pointer_sweep(): Dutch National Flag three-way partition, state =
(low, mid, high) where `low` marks the boundary past the last 0, `high`
the boundary before the first 2, and `mid` scans forward swapping each
element into its partition.
"""
from .. import algorithm as _algorithm
pointer_sweep = _algorithm.pointer_sweep


def solve(nums):
    nums = list(nums)

    def step(state):
        low, mid, high = state
        if mid > high:
            return None
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            return (low + 1, mid + 1, high)
        elif nums[mid] == 1:
            return (low, mid + 1, high)
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            return (low, mid, high - 1)

    pointer_sweep((0, 0, len(nums) - 1), step)
    return nums
