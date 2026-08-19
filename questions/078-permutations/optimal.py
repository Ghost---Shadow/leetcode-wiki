def solve(nums):
    """Optimal: backtracking via in-place swapping. Fix each position in
    turn by swapping in every remaining candidate, recursing, then
    swapping back, instead of allocating a separate 'used' array/set or
    building new lists at every step. O(n!) permutations is inherent to
    the problem; this approach minimizes auxiliary space to O(n) (the
    recursion stack) beyond the output."""
    nums = list(nums)
    n = len(nums)
    result = []

    def backtrack(start):
        if start == n:
            result.append(nums[:])
            return
        for i in range(start, n):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result
