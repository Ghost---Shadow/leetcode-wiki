"""Reshaper for questions/q014_rotting_oranges.

Converts this question's (grid) -> int I/O into a call to the shared
multi_source_bfs(): every rotten orange is a seed at minute 0, spreading to
adjacent fresh cells one minute per layer. The minutes-to-fully-rot answer
is the max minute reached, or -1 if some fresh orange is never visited.
"""
from .. import algorithm as _algorithm
multi_source_bfs = _algorithm.multi_source_bfs


def solve(grid):
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    fresh = 0
    seeds = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                seeds.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return 0

    def neighbors(state):
        r, c, minute = state
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                yield (nr, nc, minute + 1)

    newly_rotted = 0
    max_minute = 0
    for _, _, minute in multi_source_bfs(seeds, neighbors, key=lambda s: (s[0], s[1])):
        if minute > 0:
            newly_rotted += 1
            max_minute = max(max_minute, minute)

    return max_minute if newly_rotted == fresh else -1
