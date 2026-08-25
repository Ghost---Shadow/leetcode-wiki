def solve(s, p):
    """Optimal: bottom-up 2D DP. dp[i][j] means s[:i] matches p[:j]. Each cell is
    computed in O(1) from previously computed cells, so the whole table is
    filled in O(n*m) time and space, versus the brute force's exponential
    re-exploration of '*' branches."""
    n, m = len(s), len(p)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for j in range(1, m + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
            elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]

    return dp[n][m]
