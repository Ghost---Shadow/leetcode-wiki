"""Reshaper for questions/q057_time_based_key_value_store.

Converts this question's (operations, arguments) -> list replay format
into a call to the shared run_ops(): TimeMap is driven by generic
method-name dispatch (set/get), same harness as every other
design-a-class-then-replay-ops question in this technique.
"""
from .. import algorithm as _algorithm
from questions.q057_time_based_key_value_store.optimal import TimeMap

run_ops = _algorithm.run_ops


def solve(operations, arguments):
    return run_ops(TimeMap, operations, arguments)
