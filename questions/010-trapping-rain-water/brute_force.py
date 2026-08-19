def solve(height):
    """Brute-force: for each bar, scan left and right for the tallest
    neighbor bars. O(n^2)."""
    n = len(height)
    total = 0
    for i in range(n):
        left_max = max(height[:i + 1]) if i >= 0 else 0
        right_max = max(height[i:])
        total += min(left_max, right_max) - height[i]
    return total
