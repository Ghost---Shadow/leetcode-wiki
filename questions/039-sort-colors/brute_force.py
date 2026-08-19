def solve(nums):
    """Brute-force: plain bubble sort, O(n^2), instead of the one-pass
    Dutch National Flag three-pointer partition."""
    nums = list(nums)
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
