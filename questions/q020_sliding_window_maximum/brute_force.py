def solve(nums, k):
    """Brute-force: for every window position, scan all k elements to find
    the max. O(n*k) instead of the O(n) monotonic deque approach."""
    n = len(nums)
    if n == 0 or k == 0:
        return []
    result = []
    for i in range(n - k + 1):
        result.append(max(nums[i:i + k]))
    return result
