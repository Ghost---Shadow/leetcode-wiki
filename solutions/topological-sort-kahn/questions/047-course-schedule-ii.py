"""Reshaper for questions/047-course-schedule-ii.

Converts this question's (numCourses, prerequisites) -> list[int] I/O into a
call to the shared kahn_topological_order(): the answer is the topological
order itself, or [] if a cycle makes no valid order possible.
"""
import importlib.util
import os

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("algorithm", os.path.join(_here, "..", "algorithm.py"))
_algorithm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_algorithm)
kahn_topological_order = _algorithm.kahn_topological_order


def solve(numCourses, prerequisites):
    edges = [(pre, course) for course, pre in prerequisites]
    order = kahn_topological_order(numCourses, edges)
    return order if order is not None else []
