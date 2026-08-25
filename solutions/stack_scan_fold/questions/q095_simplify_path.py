"""Reshaper for questions/q095_simplify_path.

Converts this question's str -> str I/O into a call to the shared
stack_scan(): scan the '/'-separated segments, pushing real names, popping
on '..', and skipping '.' / empty segments.
"""
from .. import algorithm as _algorithm
stack_scan = _algorithm.stack_scan


def solve(path):
    def step(stack, seg):
        if seg == "" or seg == ".":
            return
        if seg == "..":
            if stack:
                stack.pop()
        else:
            stack.append(seg)

    stack = stack_scan(path.split("/"), step)
    return "/" + "/".join(stack)
