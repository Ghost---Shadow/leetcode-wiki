"""Reshaper for questions/q091_logger_rate_limiter.

Converts this question's (operations, arguments) -> list replay format
into a call to the shared run_ops(): Logger is driven by generic
method-name dispatch (shouldPrintMessage), same harness as every other
design-a-class-then-replay-ops question in this technique.
"""
from .. import algorithm as _algorithm
from questions.q091_logger_rate_limiter.optimal import Logger

run_ops = _algorithm.run_ops


def solve(operations, arguments):
    return run_ops(Logger, operations, arguments)
