def solve(nums):
    """Brute-force DP: for every index compute the min jumps needed by
    trying every reachable next index. O(n^2) instead of the O(n) greedy
    range-expansion approach."""
    n = len(nums)
    if n <= 1:
        return 0
    INF = float("inf")
    dp = [INF] * n
    dp[0] = 0
    for i in range(n):
        if dp[i] == INF:
            continue
        farthest = min(i + nums[i], n - 1)
        for j in range(i + 1, farthest + 1):
            dp[j] = min(dp[j], dp[i] + 1)
    return dp[n - 1]
