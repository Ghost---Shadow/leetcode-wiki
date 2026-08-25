"""Reshaper for questions/q028_decode_string.

Converts this question's str -> str I/O into a call to the shared
stack_scan(): push (current_string, repeat_count) frames on '[', and
pop-and-combine on ']'; the "current" string and pending digit accumulator
live in closed-over cells since they aren't the stack itself.
"""
from .. import algorithm as _algorithm
stack_scan = _algorithm.stack_scan


def solve(s):
    current = [""]
    num = [0]

    def step(stack, ch):
        if ch.isdigit():
            num[0] = num[0] * 10 + int(ch)
        elif ch == "[":
            stack.append((current[0], num[0]))
            current[0] = ""
            num[0] = 0
        elif ch == "]":
            prev_string, count = stack.pop()
            current[0] = prev_string + current[0] * count
        else:
            current[0] += ch

    stack_scan(s, step)
    return current[0]
