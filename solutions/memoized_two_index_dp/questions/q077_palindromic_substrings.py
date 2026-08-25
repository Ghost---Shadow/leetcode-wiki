"""Reshaper for questions/q077_palindromic_substrings.

Converts this question's (s) -> int I/O into a call to the shared
grid_dp(): is_pal(l, r) means s[l:r+1] is a palindrome, visited in
increasing-substring-length order so each cell's dependency (l+1, r-1)
(the inner substring) is already filled. The count of True cells is the
number of palindromic substrings.
"""
from .. import algorithm as _algorithm
grid_dp = _algorithm.grid_dp


def solve(s):
    n = len(s)
    if n == 0:
        return 0

    def compute(l, r, table):
        if l == r:
            return True
        if r == l + 1:
            return s[l] == s[r]
        return s[l] == s[r] and table[(l + 1, r - 1)]

    cells = [
        (l, l + length - 1)
        for length in range(1, n + 1)
        for l in range(0, n - length + 1)
    ]
    table = grid_dp(cells, compute)
    return sum(1 for is_pal in table.values() if is_pal)
