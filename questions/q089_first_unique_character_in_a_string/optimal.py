from collections import Counter


def solve(s):
    """Optimal: one pass to count character frequencies with a hash map, then a
    second pass to find the first character with count 1. O(n) time overall
    (two linear passes), O(1) space since the alphabet is bounded."""
    counts = Counter(s)
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1
