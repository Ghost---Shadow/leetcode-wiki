def solve(n):
    """Brute-force: naive exponential recursion that recomputes every subproblem
    from scratch with no memoization -- O(2^n) instead of O(n) DP."""
    def climb(k):
        if k <= 2:
            return k
        return climb(k - 1) + climb(k - 2)

    if n <= 0:
        return 0
    return climb(n)
