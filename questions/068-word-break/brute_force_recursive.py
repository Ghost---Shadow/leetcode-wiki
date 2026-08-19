def solve(s, wordDict):
    """Brute-force: recursively try every possible split point with no
    memoization, exploring all 2^n partitions of the string instead of the
    O(n^2) DP approach."""
    words = set(wordDict)
    n = len(s)

    def rec(i):
        if i == n:
            return True
        for j in range(i + 1, n + 1):
            if s[i:j] in words and rec(j):
                return True
        return False

    return rec(0)
