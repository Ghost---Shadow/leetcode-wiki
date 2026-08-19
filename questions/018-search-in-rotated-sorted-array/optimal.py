def solve(nums, target):
    """Modified binary search: at each step, one half of the array (split
    at mid) is guaranteed to be normally sorted, so we can decide which
    half to keep searching based on where target falls. O(log n) time,
    O(1) space."""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
