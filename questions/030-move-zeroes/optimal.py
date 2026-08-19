def solve(nums):
    """Optimal: single-pass two-pointer in-place swap. `insert_pos` tracks
    where the next nonzero element belongs; every nonzero element is swapped
    into place as we scan once left to right. O(n) time, O(1) extra space."""
    nums = list(nums)
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1
    return nums
