"""Reshaper for questions/q055_lfu_cache.

Converts this question's (operations, arguments) -> list replay format
into a call to the shared run_ops(): LFUCache is driven by generic
method-name dispatch (get/put), same harness as every other
design-a-class-then-replay-ops question in this technique.
"""
from .. import algorithm as _algorithm
from questions.q055_lfu_cache.optimal import LFUCache

run_ops = _algorithm.run_ops


def solve(operations, arguments):
    return run_ops(LFUCache, operations, arguments)
