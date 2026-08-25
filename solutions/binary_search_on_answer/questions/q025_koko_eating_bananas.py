"""Reshaper for questions/q025_koko_eating_bananas.

Converts this question's (piles, h) -> int I/O into a call to the shared
binary_search_converge(): state = (lo, hi), classic "binary search on the
answer" over eating speed, since hours_needed(speed) is monotonically
non-increasing in speed.
"""
import math

from .. import algorithm as _algorithm
binary_search_converge = _algorithm.binary_search_converge


def solve(piles, h):
    if not piles:
        return 0

    def hours_needed(speed):
        return sum(math.ceil(pile / speed) for pile in piles)

    def step(state):
        lo, hi = state
        if lo >= hi:
            return None
        mid = (lo + hi) // 2
        if hours_needed(mid) <= h:
            return (lo, mid)
        return (mid + 1, hi)

    lo, _ = binary_search_converge((1, max(piles)), step)
    return lo
