"""Reshaper for questions/q100_basic_calculator.

Converts this question's str -> int I/O into a call to the shared
stack_scan(): push (result, sign) onto the stack across parenthesis
boundaries; `result`, the pending `number`, and the current `sign` live in
closed-over cells since they aren't the stack itself.
"""
from .. import algorithm as _algorithm
stack_scan = _algorithm.stack_scan


def solve(s):
    result = [0]
    number = [0]
    sign = [1]

    def step(stack, ch):
        if ch.isdigit():
            number[0] = number[0] * 10 + int(ch)
        elif ch == "+":
            result[0] += sign[0] * number[0]
            number[0] = 0
            sign[0] = 1
        elif ch == "-":
            result[0] += sign[0] * number[0]
            number[0] = 0
            sign[0] = -1
        elif ch == "(":
            stack.append(result[0])
            stack.append(sign[0])
            result[0] = 0
            sign[0] = 1
        elif ch == ")":
            result[0] += sign[0] * number[0]
            number[0] = 0
            prev_sign = stack.pop()
            prev_result = stack.pop()
            result[0] = prev_result + prev_sign * result[0]

    stack_scan(s, step)
    result[0] += sign[0] * number[0]
    return result[0]
