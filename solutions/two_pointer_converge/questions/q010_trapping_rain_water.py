"""Reshaper for questions/q010_trapping_rain_water.

Converts this question's (height) -> int I/O into a call to the shared
converge(): step advances the side with the smaller running max inward,
tracking the running left/right max and accumulated trapped water in a
closure.
"""
from .. import algorithm as _algorithm
converge = _algorithm.converge


def solve(height):
    if not height:
        return 0

    total = 0
    left_max = height[0]
    right_max = height[-1]

    def step(left, right):
        nonlocal total, left_max, right_max
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, height[left])
            total += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            total += right_max - height[right]
        return (left, right)

    converge(0, len(height) - 1, step)
    return total
