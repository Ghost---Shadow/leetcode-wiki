"""Reshaper for questions/q094_regular_expression_matching.

Converts this question's (s, p) -> bool I/O into a call to the shared
grid_dp(): matches(i, j) means s[:i] matches p[:j], visited in row-major
order (i then j ascending) so each cell's dependencies (i-1, j-1),
(i-1, j), (i, j-2) are already filled.
"""
from .. import algorithm as _algorithm
grid_dp = _algorithm.grid_dp


def solve(s, p):
    n, m = len(s), len(p)

    def compute(i, j, table):
        if i == 0 and j == 0:
            return True
        if j == 0:
            return False
        if p[j - 1] == "*":
            val = table.get((i, j - 2), False)
            if not val and i > 0 and (p[j - 2] == "." or p[j - 2] == s[i - 1]):
                val = table.get((i - 1, j), False)
            return val
        if i == 0:
            return False
        if p[j - 1] == "." or p[j - 1] == s[i - 1]:
            return table.get((i - 1, j - 1), False)
        return False

    cells = [(i, j) for i in range(n + 1) for j in range(m + 1)]
    table = grid_dp(cells, compute)
    return table[(n, m)]
