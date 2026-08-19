def solve(nums):
    """Optimal: single pass tracking the running max AND min product ending at
    the current index (a negative number can flip a min into the new max), and
    the best answer seen so far. O(n) time, O(1) space."""
    best = cur_max = cur_min = nums[0]

    for x in nums[1:]:
        if x < 0:
            cur_max, cur_min = cur_min, cur_max
        cur_max = max(x, cur_max * x)
        cur_min = min(x, cur_min * x)
        best = max(best, cur_max)

    return best
