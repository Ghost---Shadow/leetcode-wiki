def solve(s):
    """Optimal: sliding window with a hash map of last-seen index. O(n) time, O(min(n, alphabet)) space."""
    last_seen = {}
    best = 0
    left = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best
