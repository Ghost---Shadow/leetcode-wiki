from collections import deque


def solve(nums, k):
    """Monotonic deque: keep indices of a decreasing sequence of values in
    the current window; the front is always the window max. Each index is
    pushed and popped at most once. O(n) time, O(k) space."""
    n = len(nums)
    if n == 0 or k == 0:
        return []
    dq = deque()  # stores indices, values decreasing
    result = []

    for i in range(n):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
