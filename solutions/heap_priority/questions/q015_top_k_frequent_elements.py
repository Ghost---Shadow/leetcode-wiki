"""Reshaper for questions/q015_top_k_frequent_elements.

Converts this question's (nums, k) -> list[int] I/O into a call to the
shared priority_pop_stream(): seed the frontier with (-frequency, num) for
every distinct value (negated so the heap pops highest-frequency first),
items have no successors, and the first k pops are the answer.
"""
from collections import Counter

from .. import algorithm as _algorithm
priority_pop_stream = _algorithm.priority_pop_stream


def solve(nums, k):
    counts = Counter(nums)
    seeds = [(-freq, num) for num, freq in counts.items()]

    def transition(state):
        return ()

    def priority(state):
        return state

    result = []
    for _, num in priority_pop_stream(seeds, transition, priority):
        result.append(num)
        if len(result) == k:
            break
    return result
