def solve(prices):
    """Brute-force: check every buy/sell pair. O(n^2)."""
    best = 0
    n = len(prices)
    for i in range(n):
        for j in range(i + 1, n):
            best = max(best, prices[j] - prices[i])
    return best
