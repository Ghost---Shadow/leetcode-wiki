def solve(nums, target):
    """Brute-force: scan every element linearly. O(n) instead of the
    O(log n) modified binary search that exploits the rotation."""
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1
