"""Reshaper for questions/q069_basic_calculator_ii.

Converts this question's str -> int I/O into a call to the shared
stack_scan(): items are (char, is_last_char) pairs so the step function can
flush the trailing operand the same way it flushes any other; push
signed operands on '+'/'-', fold immediately into the stack top on '*'/'/'.
"""
from .. import algorithm as _algorithm
stack_scan = _algorithm.stack_scan


def solve(s):
    op = ["+"]
    num = [0]

    def step(stack, item):
        ch, is_last = item
        if ch.isdigit():
            num[0] = num[0] * 10 + int(ch)
        if (not ch.isspace() and not ch.isdigit()) or is_last:
            if op[0] == "+":
                stack.append(num[0])
            elif op[0] == "-":
                stack.append(-num[0])
            elif op[0] == "*":
                stack.append(stack.pop() * num[0])
            elif op[0] == "/":
                prev = stack.pop()
                stack.append(int(prev / num[0]))
            op[0] = ch
            num[0] = 0

    n = len(s)
    items = [(ch, i == n - 1) for i, ch in enumerate(s)]
    stack = stack_scan(items, step)
    return sum(stack)
