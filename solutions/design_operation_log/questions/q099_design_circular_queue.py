"""Reshaper for questions/q099_design_circular_queue.

Converts this question's (operations, arguments) -> list replay format
into a call to the shared run_ops(): MyCircularQueue is driven by generic
method-name dispatch (enQueue/deQueue/Front/Rear/isEmpty/isFull), same
harness as every other design-a-class-then-replay-ops question in this
technique.
"""
from .. import algorithm as _algorithm
from questions.q099_design_circular_queue.optimal import MyCircularQueue

run_ops = _algorithm.run_ops


def solve(operations, arguments):
    return run_ops(MyCircularQueue, operations, arguments)
