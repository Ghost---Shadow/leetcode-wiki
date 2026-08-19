def solve(prices):
    """Brute-force: recursively try, on every day, both 'do nothing' and
    'buy/sell' branches with no memoization, exploring all 2^n decision
    sequences instead of the O(n) greedy sum-of-positive-diffs approach."""
    n = len(prices)

    def rec(day, holding):
        if day == n:
            return 0
        best = rec(day + 1, holding)
        if not holding:
            best = max(best, -prices[day] + rec(day + 1, True))
        else:
            best = max(best, prices[day] + rec(day + 1, False))
        return best

    return rec(0, False) if n > 0 else 0
