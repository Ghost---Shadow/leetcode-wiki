def solve(heights):
    """Brute-force: for every pair of start/end bars, track the running
    minimum height and compute the rectangle area, O(n^2) instead of the
    O(n) monotonic-stack approach."""
    n = len(heights)
    best = 0
    for i in range(n):
        min_h = heights[i]
        for j in range(i, n):
            min_h = min(min_h, heights[j])
            best = max(best, min_h * (j - i + 1))
    return best
