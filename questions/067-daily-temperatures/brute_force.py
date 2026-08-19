def solve(temperatures):
    """Brute-force: for each day, scan forward day by day until a warmer
    temperature is found, O(n^2) instead of the O(n) monotonic-stack
    approach."""
    n = len(temperatures)
    ans = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if temperatures[j] > temperatures[i]:
                ans[i] = j - i
                break
    return ans
