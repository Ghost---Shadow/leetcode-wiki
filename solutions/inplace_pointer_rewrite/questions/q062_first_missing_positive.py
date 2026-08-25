"""Reshaper for questions/q062_first_missing_positive.

Converts this question's (nums,) -> int I/O into a call to the shared
pointer_sweep(): cyclic sort, state = (i,) advancing over each index while
its step swaps the value at i into its "home" slot (value v belongs at
index v - 1) until every value that can be homed is homed.
"""
from .. import algorithm as _algorithm
pointer_sweep = _algorithm.pointer_sweep


def solve(nums):
    nums = list(nums)
    n = len(nums)

    def step(state):
        (i,) = state
        if i >= n:
            return None
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            target = nums[i] - 1
            nums[i], nums[target] = nums[target], nums[i]
        return (i + 1,)

    pointer_sweep((0,), step)

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1
