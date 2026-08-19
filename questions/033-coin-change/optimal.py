def solve(coins, amount):
    """Optimal: bottom-up dynamic programming. dp[a] = fewest coins to make
    amount a, built up from dp[0] = 0. Each amount from 1..target is computed
    once by trying each coin, reusing already-solved subproblems.
    O(amount * len(coins)) time, O(amount) space."""
    INF = float("inf")
    dp = [0] + [INF] * amount

    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a and dp[a - coin] + 1 < dp[a]:
                dp[a] = dp[a - coin] + 1

    return dp[amount] if dp[amount] != INF else -1
