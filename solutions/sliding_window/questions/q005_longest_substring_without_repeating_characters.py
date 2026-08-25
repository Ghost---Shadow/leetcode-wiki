"""Reshaper for questions/q005_longest_substring_without_repeating_characters.

Converts this question's (s) -> int I/O into a call to the shared
streaming_scan(): step(i) maintains a last-seen index map and a left
pointer, emitting the current window length at every index; the answer
is the max emission.
"""
from .. import algorithm as _algorithm
streaming_scan = _algorithm.streaming_scan


def solve(s):
    last_seen = {}
    left = 0

    def step(i):
        nonlocal left
        ch = s[i]
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = i
        return i - left + 1

    lengths = streaming_scan(len(s), step)
    return max(lengths) if lengths else 0
