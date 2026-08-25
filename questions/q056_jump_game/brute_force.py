def solve(nums):
    """Brute-force: compute reachability for every index by scanning all
    positions before it and all jump lengths from each, O(n^2) instead of
    the O(n) greedy max-reach approach."""
    n = len(nums)
    if n == 0:
        return True
    reachable = [False] * n
    reachable[0] = True
    for i in range(n):
        if not reachable[i]:
            continue
        for step in range(1, nums[i] + 1):
            if i + step < n:
                reachable[i + step] = True
    return reachable[n - 1]
