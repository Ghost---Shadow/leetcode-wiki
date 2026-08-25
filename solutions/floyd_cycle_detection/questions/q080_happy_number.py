"""Reshaper for questions/q080_happy_number.

Converts this question's (n) -> bool I/O into a call to the shared
find_cycle_meeting_point(), stepping via the digit-square-sum function.
Every chain of digit-square sums eventually cycles (either at the fixed
point 1, or the known non-1 cycle), so a meeting point always exists; n is
happy iff that meeting point is exactly 1.
"""
from .. import algorithm as _algorithm
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
