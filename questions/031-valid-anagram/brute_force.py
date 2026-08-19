def solve(s, t):
    """Brute-force: for each character in s, scan t and remove one matching
    occurrence via list.remove, instead of sorting or counting with a hash
    map. O(n^2)."""
    if len(s) != len(t):
        return False
    t_chars = list(t)
    for ch in s:
        if ch in t_chars:
            t_chars.remove(ch)
        else:
            return False
    return len(t_chars) == 0
