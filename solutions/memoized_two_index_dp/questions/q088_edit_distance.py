"""Reshaper for questions/q088_edit_distance.

Converts this question's (word1, word2) -> int I/O into a call to the
shared grid_dp(): dist(i, j) is the edit distance between word1[:i] and
word2[:j], visited in row-major order (i then j ascending) so each cell's
dependencies (i-1, j), (i, j-1), (i-1, j-1) are already filled.
"""
from .. import algorithm as _algorithm
grid_dp = _algorithm.grid_dp


def solve(word1, word2):
    n, m = len(word1), len(word2)

    def compute(i, j, table):
        if i == 0:
            return j
        if j == 0:
            return i
        if word1[i - 1] == word2[j - 1]:
            return table[(i - 1, j - 1)]
        return 1 + min(table[(i - 1, j)], table[(i, j - 1)], table[(i - 1, j - 1)])

    cells = [(i, j) for i in range(n + 1) for j in range(m + 1)]
    table = grid_dp(cells, compute)
    return table[(n, m)]
