"""Reshaper for questions/q033_coin_change.

Converts this question's (coins, amount) -> int I/O into a call to the
shared chain_dp(): fewest(a) = 1 + min(fewest(a - coin) for coin in coins
if coin <= a), the classic unbounded-knapsack recurrence over amounts
0..amount, with fewest(0) = 0.
"""
from .. import algorithm as _algorithm
chain_dp = _algorithm.chain_dp

INF = float("inf")


def solve(coins, amount):
    def compute(a, table):
        if a == 0:
            return 0
        best = INF
        for coin in coins:
            if coin <= a and table[a - coin] + 1 < best:
                best = table[a - coin] + 1
        return best

    table = chain_dp(amount, compute)
    return table[amount] if table[amount] != INF else -1
