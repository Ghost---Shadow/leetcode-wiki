def solve(nums, k):
    """Optimal: reversal algorithm. Reverse the whole array, then reverse
    the first k and remaining n-k elements separately. O(n) time, O(1)
    extra space."""
    nums = list(nums)
    n = len(nums)
    if n == 0:
        return nums
    k = k % n

    def reverse(lo, hi):
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    return nums
