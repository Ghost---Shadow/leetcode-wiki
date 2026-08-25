"""Reshaper for questions/q041_minimum_window_substring.

Converts this question's (s, t) -> str I/O into a call to the shared
streaming_scan(): step(right) admits s[right] into the window, then
contracts from the left as long as the window still satisfies all of
t's character counts, emitting (start, length) for the smallest valid
window found at this right edge; the answer is the shortest emitted
window.
"""
from collections import Counter

from .. import algorithm as _algorithm
streaming_scan = _algorithm.streaming_scan


def solve(s, t):
    if not s or not t:
        return ""

    need = Counter(t)
    missing = len(t)
    left = 0

    def step(right):
        nonlocal missing, left
        ch = s[right]
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1

        found = None
        while missing == 0:
            found = (left, right - left + 1)
            left_ch = s[left]
            need[left_ch] += 1
            if need[left_ch] > 0:
                missing += 1
            left += 1
        return found

    windows = streaming_scan(len(s), step)
    if not windows:
        return ""
    start, length = min(windows, key=lambda w: w[1])
    return s[start:start + length]
