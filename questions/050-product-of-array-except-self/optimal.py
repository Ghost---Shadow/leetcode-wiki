def solve(nums):
    """Optimal: O(n) time, O(1) extra space (excluding the output array itself).
    First fill the output array with prefix products, then sweep from the right
    multiplying in a running suffix product -- no division used."""
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result
