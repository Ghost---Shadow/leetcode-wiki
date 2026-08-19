def solve(matrix):
    """Brute-force: maintain a full 'visited' grid and, at every step,
    check all four directions to decide where to move next, instead of
    tracking tightening boundaries directly."""
    if not matrix or not matrix[0]:
        return []
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    d = 0
    r, c = 0, 0
    result = []

    for _ in range(rows * cols):
        result.append(matrix[r][c])
        visited[r][c] = True
        nr, nc = r + directions[d][0], c + directions[d][1]
        if not (0 <= nr < rows and 0 <= nc < cols) or visited[nr][nc]:
            d = (d + 1) % 4
            nr, nc = r + directions[d][0], c + directions[d][1]
        r, c = nr, nc

    return result
