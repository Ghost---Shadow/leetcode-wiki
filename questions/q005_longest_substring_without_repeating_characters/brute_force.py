def solve(s):
    """Brute-force: check every substring for repeated characters. O(n^3)."""
    n = len(s)
    best = 0
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j + 1]
            if len(set(sub)) == len(sub):
                best = max(best, len(sub))
    return best
