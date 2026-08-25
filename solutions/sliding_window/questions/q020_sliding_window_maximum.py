"""Reshaper for questions/q020_sliding_window_maximum.

Converts this question's (nums, k) -> list[int] I/O into a call to the
shared streaming_scan(): step(i) maintains a monotonic decreasing deque
of indices, evicting stale and dominated ones, emitting the window max
once the window has filled to size k.
"""
from collections import deque

from .. import algorithm as _algorithm
streaming_scan = _algorithm.streaming_scan


def solve(nums, k):
    n = len(nums)
    if n == 0 or k == 0:
        return []

    dq = deque()  # stores indices, values decreasing

    def step(i):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            return nums[dq[0]]
        return None

    return streaming_scan(n, step)
