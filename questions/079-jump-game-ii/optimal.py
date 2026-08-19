def solve(nums):
    """Optimal: greedy range expansion. Track the farthest index reachable
    within the current jump's range; when we reach the end of that range,
    take a jump and extend the boundary to the farthest reachable index
    seen so far. O(n) time, O(1) space."""
    n = len(nums)
    if n <= 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= n - 1:
                break

    return jumps
