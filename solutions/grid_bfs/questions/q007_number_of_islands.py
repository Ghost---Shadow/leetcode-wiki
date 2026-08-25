"""Reshaper for questions/q007_number_of_islands.

Converts this question's (grid) -> int I/O into a call to the shared
count_components(): each connected blob of "1" cells (4-directionally) is
one component, so the island count is just the component count over the
land cells.
"""
from .. import algorithm as _algorithm
count_components = _algorithm.count_components


def solve(grid):
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    land = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == "1"]

    def neighbors(cell):
        r, c = cell
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                yield (nr, nc)

    return count_components(land, neighbors)
