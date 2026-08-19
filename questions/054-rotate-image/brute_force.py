def solve(matrix):
    """Brute-force: builds a brand-new matrix, computing each rotated cell's
    destination with an explicit nested loop -- O(n^2) extra space instead of the
    true in-place O(1)-space transpose + reverse."""
    n = len(matrix)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - 1 - i] = matrix[i][j]
    return result
