import math


def solve(piles, h):
    """Brute-force: try every possible eating speed starting from 1,
    upward, and return the first one that finishes in time. O(n * max(piles))
    instead of binary-searching the speed."""
    if not piles:
        return 0
    max_pile = max(piles)

    def hours_needed(speed):
        return sum(math.ceil(pile / speed) for pile in piles)

    speed = 1
    while hours_needed(speed) > h:
        speed += 1
    return speed
