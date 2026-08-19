import math


def solve(piles, h):
    """Binary search on the answer (eating speed): hours_needed(speed) is
    monotonically non-increasing in speed, so binary search for the
    smallest speed that finishes within h hours. O(n log(max(piles)))
    time, O(1) extra space."""
    if not piles:
        return 0

    def hours_needed(speed):
        return sum(math.ceil(pile / speed) for pile in piles)

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if hours_needed(mid) <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo
