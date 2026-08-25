"""Reshaper for questions/q043_house_robber.

Converts this question's (nums) -> int I/O into a call to the shared
chain_dp(): best(i) = max(best(i-1), best(i-2) + nums[i]), the classic
rob-or-skip recurrence, with best(-1) = best(-2) = 0.
"""
from .. import algorithm as _algorithm
chain_dp = _algorithm.chain_dp


def solve(nums):
    if not nums:
        return 0

    n = len(nums) - 1

    def compute(i, table):
        prev1 = table[i - 1] if i - 1 >= 0 else 0
        prev2 = table[i - 2] if i - 2 >= 0 else 0
        return max(prev1, prev2 + nums[i])

    table = chain_dp(n, compute)
    return table[n]
