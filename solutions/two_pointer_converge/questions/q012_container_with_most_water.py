"""Reshaper for questions/q012_container_with_most_water.

Converts this question's (height) -> int I/O into a call to the shared
converge(): step always advances the shorter side inward, tracking the
best area seen so far in a closure.
"""
from .. import algorithm as _algorithm
converge = _algorithm.converge


def solve(height):
    best = 0

    def step(left, right):
        nonlocal best
        h = min(height[left], height[right])
        best = max(best, (right - left) * h)
        if height[left] < height[right]:
            return (left + 1, right)
        return (left, right - 1)

    converge(0, len(height) - 1, step)
    return best
