"""Reshaper for questions/q048_generate_parentheses.

Converts this question's (n) -> list[str] I/O into the state shape the
shared generate_all() engine understands, and reshapes the result back.
"""
from .. import algorithm as _algorithm
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
