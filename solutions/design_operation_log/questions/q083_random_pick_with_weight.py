"""Reshaper for questions/q083_random_pick_with_weight.

Converts this question's (operations, arguments) -> list replay format
into a call to the shared run_ops(): the question's Solution class (built
from a weight list, then repeatedly asked for pickIndex()) is driven by
generic method-name dispatch, same harness as every other
design-a-class-then-replay-ops question in this technique.
"""
from .. import algorithm as _algorithm
from questions.q083_random_pick_with_weight.optimal import Solution as _WeightedPicker

run_ops = _algorithm.run_ops


def solve(operations, arguments):
    return run_ops(_WeightedPicker, operations, arguments)
