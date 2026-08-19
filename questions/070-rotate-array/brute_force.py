def solve(nums, k):
    """Brute-force: rotate the array one step at a time, k times, O(n*k)
    instead of the O(n) three-reversal (or extra-array) approach."""
    nums = list(nums)
    n = len(nums)
    if n == 0:
        return nums
    k = k % n
    for _ in range(k):
        last = nums.pop()
        nums.insert(0, last)
    return nums
