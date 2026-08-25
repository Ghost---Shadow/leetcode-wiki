"""Reshaper for questions/q056_jump_game.

Converts this question's (nums) -> bool I/O into a call to the shared
chain_dp(): reachable(i) = (i == 0) or exists j < i with reachable(j) and
j + nums[j] >= i, a boolean-OR-over-predecessors recurrence.
"""
from .. import algorithm as _algorithm
chain_dp = _algorithm.chain_dp


def solve(nums):
    if not nums:
        return True

    n = len(nums) - 1

    def compute(i, table):
        if i == 0:
            return True
        return any(table[j] and j + nums[j] >= i for j in range(i))

    table = chain_dp(n, compute)
    return table[n]
