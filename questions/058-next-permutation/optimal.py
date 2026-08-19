def solve(nums):
    """Optimal: in-place next-permutation algorithm. Find the rightmost
    pivot where nums[i] < nums[i+1], find the smallest element to its right
    that's still greater than it, swap, then reverse the suffix. O(n) time,
    O(1) extra space."""
    nums = list(nums)
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1:] = reversed(nums[i + 1:])
    return nums
