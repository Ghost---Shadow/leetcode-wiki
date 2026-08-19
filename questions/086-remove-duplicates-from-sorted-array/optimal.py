def solve(nums):
    """Optimal: in-place two-pointer scan. `write` marks the end of the unique
    prefix built so far; each element is compared only against the last kept
    element (nums[write - 1]), not the whole result. O(n) time, O(1) extra space
    (ignoring the output list itself)."""
    if not nums:
        return []

    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1

    return nums[:write]
