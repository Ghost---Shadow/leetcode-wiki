"""Reshaper for questions/065-largest-rectangle-in-histogram.

Converts this question's (heights) -> int I/O into two calls to the shared
next_dominant_index() with dominates = "strictly smaller" (next smaller
element) -- once left-to-right for the right boundary of each bar, and once
on the reversed array for the left boundary (a standard trick: "next
smaller to the right" in the reversed array is "previous smaller to the
left" in the original).
"""
import importlib.util
import os

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("algorithm", os.path.join(_here, "..", "algorithm.py"))
_algorithm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_algorithm)
next_dominant_index = _algorithm.next_dominant_index


def solve(heights):
    n = len(heights)
    if n == 0:
        return 0

    smaller = lambda a, b: a < b

    right_smaller = next_dominant_index(heights, smaller)

    reversed_heights = heights[::-1]
    right_smaller_of_reversed = next_dominant_index(reversed_heights, smaller)
    left_smaller = [n - 1 - right_smaller_of_reversed[n - 1 - i] for i in range(n)]

    best = 0
    for i in range(n):
        left = left_smaller[i]  # index of previous smaller bar to the left, or -1
        right = right_smaller[i]  # index of next smaller bar to the right, or n
        width = right - left - 1
        best = max(best, heights[i] * width)
    return best
