def solve(n):
    """Optimal: backtracking that only ever places a parenthesis when it keeps the
    sequence valid (open count < n, close count < open count) -- this is the
    standard optimal approach, generating only valid sequences directly instead of
    generating-then-filtering. Runs in O(4^n / sqrt(n)) time, matching the number
    of valid combinations (the nth Catalan number)."""
    if n == 0:
        return [""]

    results = []
    path = []

    def backtrack(open_count, close_count):
        if len(path) == 2 * n:
            results.append("".join(path))
            return
        if open_count < n:
            path.append("(")
            backtrack(open_count + 1, close_count)
            path.pop()
        if close_count < open_count:
            path.append(")")
            backtrack(open_count, close_count + 1)
            path.pop()

    backtrack(0, 0)
    return results
