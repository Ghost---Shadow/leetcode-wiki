def solve(prices):
    """Optimal: single pass tracking the minimum price seen so far. O(n) time, O(1) space."""
    if not prices:
        return 0
    best = 0
    min_price = prices[0]
    for price in prices[1:]:
        min_price = min(min_price, price)
        best = max(best, price - min_price)
    return best
