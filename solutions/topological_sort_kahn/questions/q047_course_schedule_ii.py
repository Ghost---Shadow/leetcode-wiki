"""Reshaper for questions/q047_course_schedule_ii.

Converts this question's (numCourses, prerequisites) -> list[int] I/O into a
call to the shared kahn_topological_order(): the answer is the topological
order itself, or [] if a cycle makes no valid order possible.
"""
from .. import algorithm as _algorithm
kahn_topological_order = _algorithm.kahn_topological_order


def solve(numCourses, prerequisites):
    edges = [(pre, course) for course, pre in prerequisites]
    order = kahn_topological_order(numCourses, edges)
    return order if order is not None else []
