"""Reshaper for questions/q001_two_sum.

Converts this question's (nums, target) -> [i, j] I/O into a call to the
shared hashmap_pass(): the table maps value -> index seen so far, and the
step short-circuits with the matching pair the instant a complement is
already present.
"""
from .. import algorithm as _algorithm
hashmap_pass = _algorithm.hashmap_pass


def solve(nums, target):
    def step(table, i, num):
        complement = target - num
        if complement in table:
            return [table[complement], i]
        table[num] = i
        return None

    result, _table = hashmap_pass(nums, step)
    return result if result is not None else []
