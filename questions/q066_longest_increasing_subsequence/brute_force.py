def solve(nums):
    """Brute-force O(n^2) DP: for each index, scan all earlier indices to
    extend the best subsequence ending there, instead of the O(n log n)
    patience-sorting / binary-search approach."""
    n = len(nums)
    if n == 0:
        return 0
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
