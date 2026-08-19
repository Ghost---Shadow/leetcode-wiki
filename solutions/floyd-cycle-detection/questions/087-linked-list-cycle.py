"""Reshaper for questions/087-linked-list-cycle.

Converts this question's (values, pos) -> bool I/O into a call to the shared
find_cycle_meeting_point(), stepping via node.next.
"""
import importlib.util
import os

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("algorithm", os.path.join(_here, "..", "algorithm.py"))
_algorithm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_algorithm)
find_cycle_meeting_point = _algorithm.find_cycle_meeting_point


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(values, pos):
    if not values:
        return False

    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]

    meeting = find_cycle_meeting_point(nodes[0], lambda node: node.next)
    return meeting is not None
