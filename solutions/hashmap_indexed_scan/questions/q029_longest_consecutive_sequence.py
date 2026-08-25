"""Reshaper for questions/q029_longest_consecutive_sequence.

Converts this question's nums -> int I/O into a call to the shared
longest_chain_from_seeds(): put every number in a hash set, seed only with
numbers that start a run (predecessor absent from the set), and walk
forward while the next integer is present.
"""
from .. import algorithm as _algorithm
longest_chain_from_seeds = _algorithm.longest_chain_from_seeds


def solve(nums):
    num_set = set(nums)
    starts = [num for num in num_set if (num - 1) not in num_set]

    return longest_chain_from_seeds(
        starts,
        in_domain=lambda x: x in num_set,
        successor=lambda x: x + 1,
    )
