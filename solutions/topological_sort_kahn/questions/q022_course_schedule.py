"""Reshaper for questions/q022_course_schedule.

Converts this question's (num_courses, prerequisites) -> bool I/O into a
call to the shared kahn_topological_order(): a valid course order exists
iff there's no cycle.
"""
from .. import algorithm as _algorithm
kahn_topological_order = _algorithm.kahn_topological_order


def solve(num_courses, prerequisites):
    edges = [(pre, course) for course, pre in prerequisites]
    order = kahn_topological_order(num_courses, edges)
    return order is not None
