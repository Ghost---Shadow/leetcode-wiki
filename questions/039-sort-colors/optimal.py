def solve(nums):
    """Optimal: Dutch National Flag one-pass three-way partition. `low`
    marks the boundary past the last 0, `high` marks the boundary before the
    first 2, and `mid` scans forward, swapping each element into its
    partition. O(n) time, O(1) extra space, single pass."""
    nums = list(nums)
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums
