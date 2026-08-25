"""Reshaper for questions/q051_asteroid_collision.

Converts this question's list[int] -> list[int] I/O into a call to the
shared stack_scan(): push right-movers; when a left-mover arrives, pop and
destroy smaller right-movers off the stack top until it survives, explodes,
or destroys an equal one.
"""
from .. import algorithm as _algorithm
stack_scan = _algorithm.stack_scan


def solve(asteroids):
    def step(stack, a):
        alive = True
        while alive and a < 0 and stack and stack[-1] > 0:
            if stack[-1] < -a:
                stack.pop()
                continue
            elif stack[-1] == -a:
                stack.pop()
            alive = False
        if alive:
            stack.append(a)

    return stack_scan(asteroids, step)
