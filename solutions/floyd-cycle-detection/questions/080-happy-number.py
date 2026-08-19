"""Reshaper for questions/080-happy-number.

Converts this question's (n) -> bool I/O into a call to the shared
find_cycle_meeting_point(), stepping via the digit-square-sum function.
Every chain of digit-square sums eventually cycles (either at the fixed
point 1, or the known non-1 cycle), so a meeting point always exists; n is
happy iff that meeting point is exactly 1.
"""
import importlib.util
import os

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("algorithm", os.path.join(_here, "..", "algorithm.py"))
_algorithm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_algorithm)
find_cycle_meeting_point = _algorithm.find_cycle_meeting_point


def digit_square_sum(x):
    total = 0
    while x > 0:
        digit = x % 10
        total += digit * digit
        x //= 10
    return total


def solve(n):
    meeting = find_cycle_meeting_point(n, digit_square_sum)
    return meeting == 1
