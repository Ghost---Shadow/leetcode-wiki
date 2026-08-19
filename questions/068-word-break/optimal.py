def solve(s, wordDict):
    """Optimal: bottom-up DP where dp[i] means s[:i] can be segmented.
    A set gives O(1) average word lookups. O(n^2) time (n^2 substring
    slices in the worst case), O(n) space for the DP table."""
    words = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break

    return dp[n]
