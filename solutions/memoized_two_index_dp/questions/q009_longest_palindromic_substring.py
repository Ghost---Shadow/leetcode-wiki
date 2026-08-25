"""Reshaper for questions/q009_longest_palindromic_substring.

Converts this question's (s) -> str I/O into a call to the shared
grid_dp(): is_pal(l, r) means s[l:r+1] is a palindrome, visited in
increasing-substring-length order so each cell's dependency (l+1, r-1)
(the inner substring) is already filled.
"""
from .. import algorithm as _algorithm
grid_dp = _algorithm.grid_dp


def solve(s):
    n = len(s)
    if n == 0:
        return ""

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

    best_len, best_start = 1, 0
    for (l, r), is_pal in table.items():
        if is_pal and r - l + 1 > best_len:
            best_len, best_start = r - l + 1, l
    return s[best_start:best_start + best_len]
