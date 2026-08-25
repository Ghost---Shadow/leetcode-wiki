"""Reshaper for questions/q053_merge_sorted_array.

Converts this question's (nums1, m, nums2, n) -> list[int] I/O into a call
to the shared scan(): items are the destination slots m+n-1 down to 0,
and combine() (ignoring its own accumulator; the real state -- the two
source pointers -- lives in the closure) writes the larger of the two
current tail candidates into each slot, from the back.
"""
from .. import algorithm as _algorithm
scan = _algorithm.scan


def solve(nums1, m, nums2, n):
    nums1 = list(nums1)
    nums2 = list(nums2)
    i, j = m - 1, n - 1

    def combine(_, k):
        nonlocal i, j
        if j < 0:
            return None
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        return None

    scan(list(range(m + n - 1, -1, -1)), None, combine)
    return nums1
