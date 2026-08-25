def solve(nums):
    """Kadane's algorithm: track the best subarray sum ending at each
    index, extending the previous run or restarting here. O(n) time,
    O(1) space."""
    if not nums:
        return 0
    best = nums[0]
    current = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        best = max(best, current)
    return best
