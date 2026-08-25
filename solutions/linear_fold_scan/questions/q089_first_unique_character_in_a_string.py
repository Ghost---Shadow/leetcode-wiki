"""Reshaper for questions/q089_first_unique_character_in_a_string.

Converts this question's (s) -> int I/O into two calls to the shared
linear_fold(): one pass builds character frequency counts, a second pass
folds over (index, char) pairs keeping the first index whose count is 1.
"""
from .. import algorithm as _algorithm
linear_fold = _algorithm.linear_fold


def solve(s):
    def count_step(counts, ch):
        counts[ch] = counts.get(ch, 0) + 1
        return counts

    counts = linear_fold(s, {}, count_step)

    def find_step(found, item):
        if found != -1:
            return found
        i, ch = item
        return i if counts[ch] == 1 else -1

    return linear_fold(list(enumerate(s)), -1, find_step)
