def solve(nums):
    """Brute-force: repeatedly scan from the start looking for a zero
    followed by a nonzero and bubble it forward one step at a time,
    instead of a single-pass two-pointer swap. O(n^2)."""
    nums = list(nums)
    n = len(nums)
    changed = True
    while changed:
        changed = False
        for i in range(n - 1):
            if nums[i] == 0 and nums[i + 1] != 0:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                changed = True
    return nums
