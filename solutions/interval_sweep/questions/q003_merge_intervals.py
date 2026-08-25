"""Reshaper for questions/q003_merge_intervals.

Converts this question's intervals -> merged intervals I/O into a call to
the shared sweep_sorted(): sort by start, then fold a running "merged
output list" -- extend the last interval on overlap, otherwise append a
new one.
"""
from .. import algorithm as _algorithm
sweep_sorted = _algorithm.sweep_sorted


def solve(intervals):
    def step(merged, iv):
        start, end = iv
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
        return merged

    return sweep_sorted(intervals, key=lambda iv: iv[0], init_state=[], step=step)
