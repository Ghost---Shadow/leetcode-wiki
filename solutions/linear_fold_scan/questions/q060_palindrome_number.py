"""Reshaper for questions/q060_palindrome_number.

Converts this question's (x) -> bool I/O into a call to the shared
linear_fold(): folds over the decimal digits of x, building their
reversal; x is a palindrome iff it's non-negative and equals its own
digit reversal.
"""
from .. import algorithm as _algorithm
linear_fold = _algorithm.linear_fold


def solve(x):
    if x < 0:
        return False

    # Fold over the digits in reverse (right-to-left) order: accumulating
    # acc = acc * 10 + d while consuming right-to-left reconstructs the
    # digit-reversed number.
    digits = [int(d) for d in str(x)][::-1]

    def step(acc, d):
        return acc * 10 + d

    reversed_x = linear_fold(digits, 0, step)
    return reversed_x == x
