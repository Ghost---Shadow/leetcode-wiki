"""Reshaper for questions/048-generate-parentheses.

Converts this question's (n) -> list[str] I/O into the state shape the
shared generate_all() engine understands, and reshapes the result back.
"""
import importlib.util
import os

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("algorithm", os.path.join(_here, "..", "algorithm.py"))
_algorithm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_algorithm)
generate_all = _algorithm.generate_all


def solve(n):
    if n == 0:
        return [""]

    def expand(state):
        s, opened, closed = state
        options = []
        if opened < n:
            no, nc = opened + 1, closed
            options.append(((s + "(", no, nc), no == n and nc == n))
        if closed < opened:
            no, nc = opened, closed + 1
            options.append(((s + ")", no, nc), no == n and nc == n))
        return options

    results = generate_all(("", 0, 0), expand)
    return [s for s, _, _ in results]
