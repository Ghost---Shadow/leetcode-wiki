from collections import Counter


def solve(s, t):
    """Brute-force: checks every substring of s for containing all characters of t
    (with multiplicity), keeping the shortest match -- O(n^3) instead of the O(n)
    sliding-window approach."""
    if not s or not t:
        return ""
    need = Counter(t)
    n = len(s)
    best = ""
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j + 1]
            if len(sub) < len(t):
                continue
            if best and len(sub) >= len(best):
                continue
            have = Counter(sub)
            if all(have[ch] >= cnt for ch, cnt in need.items()):
                best = sub
    return best
