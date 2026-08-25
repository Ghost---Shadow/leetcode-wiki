"""Reshaper for questions/q017_merge_k_sorted_lists.

Converts this question's list-of-plain-lists -> merged list I/O into a call
to the shared priority_pop_stream(): seed the frontier with the head of
each list, and each pop's transition releases that same list's next
element -- a k-way merge is exactly "always take the smallest available
head, and reveal what comes after it".
"""
from .. import algorithm as _algorithm
priority_pop_stream = _algorithm.priority_pop_stream


def solve(lists):
    seeds = []
    for list_index, values in enumerate(lists):
        if values:
            seeds.append((values[0], list_index, 0))

    def transition(state):
        _, list_index, elem_index = state
        values = lists[list_index]
        next_index = elem_index + 1
        if next_index < len(values):
            return ((values[next_index], list_index, next_index),)
        return ()

    def priority(state):
        val, list_index, _ = state
        return (val, list_index)

    return [val for val, _, _ in priority_pop_stream(seeds, transition, priority)]
