"""Reshaper for questions/q084_design_hit_counter.

Converts this question's (operations, arguments) -> list replay format
into a call to the shared run_ops(): HitCounter is driven by generic
method-name dispatch (hit/getHits), same harness as every other
design-a-class-then-replay-ops question in this technique.
"""
from .. import algorithm as _algorithm
from questions.q084_design_hit_counter.optimal import HitCounter

run_ops = _algorithm.run_ops


def solve(operations, arguments):
    return run_ops(HitCounter, operations, arguments)
