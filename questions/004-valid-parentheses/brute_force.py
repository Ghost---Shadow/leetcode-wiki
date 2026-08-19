def solve(s):
    """Brute-force: repeatedly delete adjacent matching pairs from the string
    until none remain; valid iff the string reduces to empty. O(n^2)."""
    pairs = ("()", "[]", "{}")
    changed = True
    while changed:
        changed = False
        for p in pairs:
            idx = s.find(p)
            if idx != -1:
                s = s[:idx] + s[idx + 2:]
                changed = True
    return s == ""
