"""Reshaper for questions/q049_climbing_stairs.

Converts this question's (n) -> int I/O into a call to the shared
chain_dp(): ways(i) is the Fibonacci-style recurrence
ways(i) = ways(i-1) + ways(i-2), with ways(0) = ways(1) = 1.
"""
from .. import algorithm as _algorithm
chain_dp = _algorithm.chain_dp


def solve(n):
    if n <= 0:
        return 0

    def compute(i, table):
        if i <= 1:
            return 1
        return table[i - 1] + table[i - 2]

    table = chain_dp(n, compute)
    return table[n]
