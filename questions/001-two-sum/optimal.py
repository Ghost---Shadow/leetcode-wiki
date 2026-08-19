def solve(nums, target):
    """Optimal: single pass with a hash map from value -> index. O(n) time, O(n) space."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
