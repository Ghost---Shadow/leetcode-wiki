def solve(height):
    """Brute-force: check every pair of lines for the max area. O(n^2)."""
    n = len(height)
    best = 0
    for i in range(n):
        for j in range(i + 1, n):
            area = (j - i) * min(height[i], height[j])
            best = max(best, area)
    return best
