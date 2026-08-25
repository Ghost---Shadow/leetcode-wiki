"""Reshaper for questions/q066_longest_increasing_subsequence.

Converts this question's (nums) -> int I/O into a call to the shared
chain_dp(): length(i) = 1 + max(length(j) for j < i if nums[j] < nums[i]),
the classic O(n^2) LIS-ending-at-i recurrence.
"""
from .. import algorithm as _algorithm
chain_dp = _algorithm.chain_dp


def solve(nums):
    if not nums:
        return 0

    n = len(nums) - 1

    def compute(i, table):
        best = 0
        for j in range(i):
            if nums[j] < nums[i] and table[j] > best:
                best = table[j]
        return best + 1

    table = chain_dp(n, compute)
    return max(table.values())
