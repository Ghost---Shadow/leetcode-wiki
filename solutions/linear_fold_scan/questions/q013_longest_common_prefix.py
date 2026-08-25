"""Reshaper for questions/q013_longest_common_prefix.

Converts this question's (strs) -> str I/O into a call to the shared
linear_fold(): folds over the columns of strs[0], appending a character
to the prefix while every other string still agrees at that column, and
leaving the prefix unchanged (via a closed-over "stopped" flag) once a
mismatch is found.
"""
from .. import algorithm as _algorithm
linear_fold = _algorithm.linear_fold


def solve(strs):
    if not strs:
        return ""

    stopped = [False]

    def step(prefix, item):
        i, ch = item
        if stopped[0]:
            return prefix
        for other in strs[1:]:
            if i >= len(other) or other[i] != ch:
                stopped[0] = True
                return prefix
        return prefix + ch

    return linear_fold(list(enumerate(strs[0])), "", step)
