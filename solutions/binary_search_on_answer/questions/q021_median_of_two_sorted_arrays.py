"""Reshaper for questions/q021_median_of_two_sorted_arrays.

Converts this question's (nums1, nums2) -> float I/O into a call to the
shared binary_search_converge(): state = (lo, hi, answer), binary-searching
the partition index `i` in the smaller array; `answer` stays None until a
valid partition (every left element <= every right element) is found.
"""
from .. import algorithm as _algorithm
binary_search_converge = _algorithm.binary_search_converge


def solve(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total = m + n
    half = (total + 1) // 2

    def step(state):
        lo, hi, answer = state
        if answer is not None or lo > hi:
            return None
        i = (lo + hi) // 2
        j = half - i

        left1 = nums1[i - 1] if i > 0 else float("-inf")
        right1 = nums1[i] if i < m else float("inf")
        left2 = nums2[j - 1] if j > 0 else float("-inf")
        right2 = nums2[j] if j < n else float("inf")

        if left1 <= right2 and left2 <= right1:
            if total % 2 == 1:
                return (lo, hi, float(max(left1, left2)))
            return (lo, hi, (max(left1, left2) + min(right1, right2)) / 2.0)
        elif left1 > right2:
            return (lo, i - 1, None)
        else:
            return (i + 1, hi, None)

    _, _, answer = binary_search_converge((0, m, None), step)
    return answer if answer is not None else 0.0
