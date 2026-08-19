def solve(nums):
    """Brute-force: computes the product of every contiguous subarray, O(n^2),
    instead of the O(n) running max/min DP that handles sign flips."""
    n = len(nums)
    best = nums[0]
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= nums[j]
            best = max(best, prod)
    return best
