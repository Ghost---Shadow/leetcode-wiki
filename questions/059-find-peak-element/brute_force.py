def solve(nums):
    """Brute-force: linearly scan every index and compare against both
    neighbors, O(n) instead of the O(log n) binary search approach."""
    n = len(nums)
    for i in range(n):
        left = nums[i - 1] if i - 1 >= 0 else float("-inf")
        right = nums[i + 1] if i + 1 < n else float("-inf")
        if nums[i] > left and nums[i] > right:
            return i
    return -1
