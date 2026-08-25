def solve(s):
    """Brute-force: check every substring for being a palindrome. O(n^3)."""
    n = len(s)
    best = ""
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j + 1]
            if len(sub) > len(best) and sub == sub[::-1]:
                best = sub
    return best
