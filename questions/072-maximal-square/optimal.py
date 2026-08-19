def solve(matrix):
    """Optimal: DP where dp[i][j] is the side length of the largest square
    whose bottom-right corner is (i, j). dp[i][j] = min(dp[i-1][j],
    dp[i][j-1], dp[i-1][j-1]) + 1 when matrix[i][j] == '1'. O(rows*cols)
    time. Uses a single rolling row (O(cols) space) instead of a full 2D
    table."""
    if not matrix or not matrix[0]:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    prev = [0] * (cols + 1)
    best = 0
    for i in range(rows):
        curr = [0] * (cols + 1)
        for j in range(cols):
            if matrix[i][j] == "1":
                curr[j + 1] = min(prev[j + 1], curr[j], prev[j]) + 1
                best = max(best, curr[j + 1])
        prev = curr
    return best * best
