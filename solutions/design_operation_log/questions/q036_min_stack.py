"""Reshaper for questions/q036_min_stack.

Converts this question's (operations, arguments) -> list replay format
into a call to the shared run_ops(): MinStack is driven by generic
method-name dispatch (push/pop/top/getMin), same harness as every other
design-a-class-then-replay-ops question in this technique.
"""
from .. import algorithm as _algorithm
from questions.q036_min_stack.optimal import MinStack

run_ops = _algorithm.run_ops


def solve(operations, arguments):
    return run_ops(MinStack, operations, arguments)
