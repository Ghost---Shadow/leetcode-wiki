def solve(word1, word2):
    """Optimal: bottom-up DP with a rolling 2-row buffer. dp[j] holds the edit
    distance between word1[:i] and word2[:j]; only the previous row is ever
    needed, so we keep just two rows (swapped each iteration) instead of a full
    n*m table. To minimize the row width we always roll over the shorter word.
    O(n*m) time, O(min(n, m)) space."""
    if len(word1) < len(word2):
        word1, word2 = word2, word1

    n, m = len(word1), len(word2)
    prev = list(range(m + 1))

    for i in range(1, n + 1):
        curr = [i] + [0] * m
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
        prev = curr

    return prev[m]
