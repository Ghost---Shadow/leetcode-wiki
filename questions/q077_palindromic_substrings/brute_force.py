def solve(s):
    """Brute-force: check every substring for being a palindrome. O(n^3)
    instead of the O(n^2) expand-around-center (or DP) approach."""
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j + 1]
            if sub == sub[::-1]:
                count += 1
    return count
