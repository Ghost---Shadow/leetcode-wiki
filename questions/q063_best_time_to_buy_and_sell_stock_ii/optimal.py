def solve(prices):
    """Optimal: greedily sum every positive day-to-day price difference —
    equivalent to capturing every upward run. O(n) time, O(1) space."""
    total = 0
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i - 1]
        if diff > 0:
            total += diff
    return total
