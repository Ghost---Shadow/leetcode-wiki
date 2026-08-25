from collections import Counter


def solve(s, t):
    """Optimal: compare character-frequency counts built in a single pass
    over each string, instead of sorting or repeated linear removal.
    O(n) time, O(1) extra space (bounded alphabet)."""
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)
