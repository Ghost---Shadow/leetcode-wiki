"""Reshaper for questions/q037_valid_palindrome.

Converts this question's (s) -> bool I/O into a call to the shared
converge(): step skips non-alphanumeric characters in place from both
sides before comparing, and signals early stop (via returning None) as
soon as a mismatch is found, recording the failure in a closure.
"""
from .. import algorithm as _algorithm
converge = _algorithm.converge


def solve(s):
    ok = True

    def step(left, right):
        nonlocal ok
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            ok = False
            return None
        return (left + 1, right - 1)

    converge(0, len(s) - 1, step)
    return ok
