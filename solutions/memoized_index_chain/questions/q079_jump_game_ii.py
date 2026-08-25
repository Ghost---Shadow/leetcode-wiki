"""Reshaper for questions/q079_jump_game_ii.

Converts this question's (nums) -> int I/O into a call to the shared
chain_dp(): hops(i) = 1 + min(hops(j) for j < i if j + nums[j] >= i), the
min-over-predecessors recurrence for fewest jumps to reach index i.
"""
from .. import algorithm as _algorithm
chain_dp = _algorithm.chain_dp

INF = float("inf")


def solve(nums):
    n = len(nums)
    if n <= 1:
        return 0

    last = n - 1

    def compute(i, table):
        if i == 0:
            return 0
        best = INF
        for j in range(i):
            if j + nums[j] >= i and table[j] + 1 < best:
                best = table[j] + 1
        return best

    table = chain_dp(last, compute)
    return table[last]
