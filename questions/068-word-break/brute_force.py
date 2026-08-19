def solve(s, wordDict):
    """Brute-force: explores every possible split point via an explicit stack
    of "next start index" states instead of recursion -- no visited/memo set,
    so the same 2^n partitions get explored as the recursive version."""
    words = set(wordDict)
    n = len(s)

    stack = [0]
    while stack:
        i = stack.pop()
        if i == n:
            return True
        for j in range(i + 1, n + 1):
            if s[i:j] in words:
                stack.append(j)
    return False
