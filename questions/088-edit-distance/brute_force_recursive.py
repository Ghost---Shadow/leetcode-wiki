def solve(word1, word2):
    """Brute-force recursion without memoization: explores every insert/delete/replace
    sequence, exponential time, instead of the O(n*m) bottom-up DP."""
    def helper(i, j):
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i
        if word1[i] == word2[j]:
            return helper(i + 1, j + 1)
        return 1 + min(
            helper(i + 1, j),      # delete
            helper(i, j + 1),      # insert
            helper(i + 1, j + 1),  # replace
        )

    return helper(0, 0)
