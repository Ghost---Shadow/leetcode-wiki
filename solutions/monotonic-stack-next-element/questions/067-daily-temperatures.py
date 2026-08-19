"""Reshaper for questions/067-daily-temperatures.

Converts this question's (temperatures) -> list[int] I/O into a call to the
shared next_dominant_index() with dominates = "strictly greater" (next
greater element), and reshapes indices back into day-counts.
"""
import importlib.util
import os

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("algorithm", os.path.join(_here, "..", "algorithm.py"))
_algorithm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_algorithm)
next_dominant_index = _algorithm.next_dominant_index


def solve(temperatures):
    n = len(temperatures)
    nxt = next_dominant_index(temperatures, lambda a, b: a > b)
    return [(nxt[i] - i) if nxt[i] < n else 0 for i in range(n)]
