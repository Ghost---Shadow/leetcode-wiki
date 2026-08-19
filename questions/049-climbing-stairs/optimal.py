def solve(n):
    """Optimal: O(n) time, O(1) space using two rolling variables (this is
    essentially the Fibonacci recurrence) instead of exponential recursion or a
    memoization dict."""
    if n <= 0:
        return 0
    prev2, prev1 = 0, 1
    for _ in range(n):
        prev2, prev1 = prev1, prev2 + prev1
    return prev1
