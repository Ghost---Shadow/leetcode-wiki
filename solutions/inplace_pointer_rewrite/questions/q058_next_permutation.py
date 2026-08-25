"""Reshaper for questions/q058_next_permutation.

Converts this question's (nums,) -> list[int] I/O into a call to the
shared pointer_sweep(): after locating the pivot and its swap target with
a plain scan, the suffix is reversed via the same inward-converging
two-pointer sweep used elsewhere in this technique.
"""
from .. import algorithm as _algorithm
pointer_sweep = _algorithm.pointer_sweep


def solve(nums):
    nums = list(nums)
    n = len(nums)

    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    def step(state):
        l, h = state
        if l >= h:
            return None
        nums[l], nums[h] = nums[h], nums[l]
        return (l + 1, h - 1)

    pointer_sweep((i + 1, n - 1), step)
    return nums
