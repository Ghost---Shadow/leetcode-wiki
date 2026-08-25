"""Reshaper for questions/q004_valid_parentheses.

Converts this question's str -> bool I/O into a call to the shared
stack_scan(): push opening brackets, and on a closing bracket pop-and-match
against the expected opener, tracking a validity flag in a closed-over cell.
"""
from .. import algorithm as _algorithm
stack_scan = _algorithm.stack_scan


def solve(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    ok = [True]

    def step(stack, ch):
        if not ok[0]:
            return
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                ok[0] = False
        else:
            stack.append(ch)

    stack = stack_scan(s, step)
    return ok[0] and not stack
