def solve(nums):
    """Optimal: O(n) time, O(1) space DP using two rolling variables instead of a
    full DP array or memo dict. prev2 = best up to i-2, prev1 = best up to i-1."""
    prev2, prev1 = 0, 0
    for num in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + num)
    return prev1
