"""Reshaper for questions/q002_lru_cache.

Converts this question's (operations, arguments) -> list replay format
into a call to the shared run_ops(): LRUCache is driven by generic
method-name dispatch, identical to every other design-a-class-then-
replay-ops question in this technique.
"""
from .. import algorithm as _algorithm
from questions.q002_lru_cache.optimal import LRUCache

run_ops = _algorithm.run_ops


def solve(operations, arguments):
    return run_ops(LRUCache, operations, arguments)
