def solve(nums):
    """Optimal: binary search exploiting that any edge with an ascending
    neighbor leads toward a peak. O(log n) time, O(1) space."""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo
