"""Reshaper for questions/q067_daily_temperatures.

Converts this question's (temperatures) -> list[int] I/O into a call to the
shared next_dominant_index() with dominates = "strictly greater" (next
greater element), and reshapes indices back into day-counts.
"""
from .. import algorithm as _algorithm
next_dominant_index = _algorithm.next_dominant_index


def solve(temperatures):
    n = len(temperatures)
    nxt = next_dominant_index(temperatures, lambda a, b: a > b)
    return [(nxt[i] - i) if nxt[i] < n else 0 for i in range(n)]
