def solve(temperatures):
    """Optimal: monotonic decreasing stack of indices whose warmer day
    hasn't been found yet. O(n) time, O(n) space."""
    n = len(temperatures)
    ans = [0] * n
    stack = []

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)

    return ans
