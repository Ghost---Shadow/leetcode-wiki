"""Reshaper for questions/022-course-schedule.

Converts this question's (num_courses, prerequisites) -> bool I/O into a
call to the shared kahn_topological_order(): a valid course order exists
iff there's no cycle.
"""
import importlib.util
import os

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("algorithm", os.path.join(_here, "..", "algorithm.py"))
_algorithm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_algorithm)
kahn_topological_order = _algorithm.kahn_topological_order


def solve(num_courses, prerequisites):
    edges = [(pre, course) for course, pre in prerequisites]
    order = kahn_topological_order(num_courses, edges)
    return order is not None
