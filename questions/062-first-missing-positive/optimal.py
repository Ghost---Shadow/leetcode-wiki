def solve(nums):
    """Optimal: cyclic sort — place each value v (1 <= v <= n) at index
    v - 1 in-place, then scan for the first index whose value doesn't
    match. O(n) time, O(1) extra space."""
    nums = list(nums)
    n = len(nums)

    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            target = nums[i] - 1
            nums[i], nums[target] = nums[target], nums[i]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1
