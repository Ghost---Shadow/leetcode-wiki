"""Reshaper for questions/q042_roman_to_integer.

Converts this question's (s) -> int I/O into a call to the shared
linear_fold(): folds over (value, next_value) lookahead pairs built from
s, subtracting a symbol's value when it's smaller than the value that
follows it and adding it otherwise.
"""
from .. import algorithm as _algorithm
linear_fold = _algorithm.linear_fold

VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def solve(s):
    vals = [VALUES[ch] for ch in s]
    pairs = [
        (vals[i], vals[i + 1] if i + 1 < len(vals) else 0)
        for i in range(len(vals))
    ]

    def step(total, pair):
        cur, nxt = pair
        return total - cur if cur < nxt else total + cur

    return linear_fold(pairs, 0, step)
