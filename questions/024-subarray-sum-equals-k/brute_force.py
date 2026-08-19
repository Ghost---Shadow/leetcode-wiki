def solve(nums, k):
    """Brute-force: check every contiguous subarray's sum directly. O(n^2)
    instead of the O(n) prefix-sum + hash map approach."""
    n = len(nums)
    count = 0
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total == k:
                count += 1
    return count
