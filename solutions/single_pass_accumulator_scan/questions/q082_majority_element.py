"""Reshaper for questions/q082_majority_element.

Converts this question's (nums,) -> int I/O into a call to the shared
scan(): Boyer-Moore voting, accumulator = running count, with the current
candidate tracked in the closure -- reset the candidate whenever count
hits zero, otherwise increment/decrement based on a match.
"""
from .. import algorithm as _algorithm
scan = _algorithm.scan


def solve(nums):
    candidate = None

    def combine(count, x):
        nonlocal candidate
        if count == 0:
            candidate = x
        return count + 1 if x == candidate else count - 1

    scan(nums, 0, combine)
    return candidate
