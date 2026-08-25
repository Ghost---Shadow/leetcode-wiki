"""Reshaper for questions/q027_kth_largest_element_in_an_array.

Converts this question's (nums, k) -> int I/O into a call to the shared
priority_pop_stream(): seed the frontier with every negated value (items
have no successors), and the k-th pop is the k-th largest original value.
"""
from .. import algorithm as _algorithm
priority_pop_stream = _algorithm.priority_pop_stream


def solve(nums, k):
    seeds = [-num for num in nums]

    def transition(state):
        return ()

    def priority(state):
        return state

    stream = priority_pop_stream(seeds, transition, priority)
    value = None
    for _ in range(k):
        value = next(stream)
    return -value
