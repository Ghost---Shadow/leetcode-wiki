"""Reshaper for questions/q072_maximal_square.

Converts this question's (matrix) -> int I/O into a call to the shared
grid_dp(): side(i, j) is the side length of the largest all-'1' square
whose bottom-right corner is (i, j), visited in row-major order so each
cell's dependencies (i-1, j), (i, j-1), (i-1, j-1) are already filled.
"""
from .. import algorithm as _algorithm
grid_dp = _algorithm.grid_dp


def solve(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])

    def compute(i, j, table):
        if matrix[i][j] != "1":
            return 0
        up = table.get((i - 1, j), 0)
        left = table.get((i, j - 1), 0)
        diag = table.get((i - 1, j - 1), 0)
        return min(up, left, diag) + 1

    cells = [(i, j) for i in range(rows) for j in range(cols)]
    table = grid_dp(cells, compute)
    best = max(table.values()) if table else 0
    return best * best
