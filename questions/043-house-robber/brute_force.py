def solve(nums):
    """Brute-force: enumerates all 2^n subsets via bitmask, discards any subset with
    two adjacent picks, keeps the max sum among the rest -- O(2^n * n) instead of
    O(n) DP."""
    n = len(nums)
    best = 0
    for mask in range(1 << n):
        valid = True
        total = 0
        for i in range(n):
            if mask & (1 << i):
                if i > 0 and mask & (1 << (i - 1)):
                    valid = False
                    break
                total += nums[i]
        if valid:
            best = max(best, total)
    return best
