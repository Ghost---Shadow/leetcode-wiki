def solve(grid):
    """Brute-force: repeatedly sweep the entire grid, rotting any fresh
    orange adjacent to a rotten one, until a full sweep changes nothing.
    O(n^2 * m^2) instead of a single multi-source BFS."""
    if not grid or not grid[0]:
        return 0
    grid = [row[:] for row in grid]
    rows, cols = len(grid), len(grid[0])
    minutes = 0

    def has_fresh():
        return any(cell == 1 for row in grid for cell in row)

    while has_fresh():
        to_rot = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            to_rot.append((nr, nc))
        if not to_rot:
            return -1
        for r, c in to_rot:
            grid[r][c] = 2
        minutes += 1

    return minutes
