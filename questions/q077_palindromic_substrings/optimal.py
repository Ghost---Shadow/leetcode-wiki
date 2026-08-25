def solve(s):
    """Optimal: expand around center. For each of the 2n-1 possible centers
    (each index, and each gap between adjacent indices), expand outward
    while characters match. O(n^2) time, O(1) space -- the standard optimal
    non-Manacher approach."""
    n = len(s)
    count = 0

    def expand(l, r):
        nonlocal count
        while l >= 0 and r < n and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

    for center in range(n):
        expand(center, center)      # odd-length palindromes
        expand(center, center + 1)  # even-length palindromes

    return count
