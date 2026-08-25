import bisect


def solve(nums, target):
    """Optimal: two binary searches (bisect_left / bisect_right) to find
    the target's bounds. O(log n) time, O(1) extra space."""
    left = bisect.bisect_left(nums, target)
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    right = bisect.bisect_right(nums, target) - 1
    return [left, right]
