"""Reshaper for questions/q034_insert_delete_getrandom_o_1.

Converts this question's (operations, arguments) -> list replay format
into a call to the shared run_ops(): RandomizedSet is driven by generic
method-name dispatch (insert/remove/getRandom), same harness as every
other design-a-class-then-replay-ops question in this technique.
"""
from .. import algorithm as _algorithm
from questions.q034_insert_delete_getrandom_o_1.optimal import RandomizedSet

run_ops = _algorithm.run_ops


def solve(operations, arguments):
    return run_ops(RandomizedSet, operations, arguments)
