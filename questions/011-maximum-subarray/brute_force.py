def solve(nums):
    """Brute-force: check every contiguous subarray's sum. O(n^2)."""
    n = len(nums)
    best = nums[0] if nums else 0
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            best = max(best, total)
    return best
