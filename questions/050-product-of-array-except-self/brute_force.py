def solve(nums):
    """Brute-force: for each index, multiplies every other element in a fresh
    inner loop -- O(n^2) instead of the O(n) prefix/suffix product pass, and
    doesn't rely on division."""
    n = len(nums)
    result = []
    for i in range(n):
        prod = 1
        for j in range(n):
            if j != i:
                prod *= nums[j]
        result.append(prod)
    return result
