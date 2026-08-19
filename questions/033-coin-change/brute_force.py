def solve(coins, amount):
    """Brute-force recursion without memoization: tries every coin at every
    remaining amount, recomputing overlapping subproblems from scratch.
    Exponential time O(k^amount) instead of O(amount * k) DP."""
    import sys
    sys.setrecursionlimit(10000)

    def helper(remaining):
        if remaining == 0:
            return 0
        if remaining < 0:
            return float("inf")
        best = float("inf")
        for coin in coins:
            result = helper(remaining - coin)
            if result != float("inf"):
                best = min(best, result + 1)
        return best

    result = helper(amount)
    return result if result != float("inf") else -1
