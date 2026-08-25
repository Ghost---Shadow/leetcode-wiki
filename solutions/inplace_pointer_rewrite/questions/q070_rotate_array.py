"""Reshaper for questions/q070_rotate_array.

Converts this question's (nums, k) -> list[int] I/O into three calls to
the shared pointer_sweep(): the reversal trick rotates by reversing the
whole array, then reversing the first k and remaining n-k elements
separately, each reversal itself a pair of inward-converging pointers.
"""
from .. import algorithm as _algorithm
pointer_sweep = _algorithm.pointer_sweep


def solve(nums, k):
    nums = list(nums)
    n = len(nums)
    if n == 0:
        return nums
    k = k % n

    def reverse(lo, hi):
        def step(state):
            l, h = state
            if l >= h:
                return None
            nums[l], nums[h] = nums[h], nums[l]
            return (l + 1, h - 1)

        pointer_sweep((lo, hi), step)

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    return nums
