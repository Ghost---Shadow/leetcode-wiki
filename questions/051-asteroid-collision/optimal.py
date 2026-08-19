def solve(asteroids):
    """Optimal: single-pass stack simulation. Push right-movers; when a
    left-mover arrives, pop and destroy smaller right-movers off the stack top
    until it either survives, explodes, or destroys an equal one -- O(n) time
    (each element pushed/popped at most once), O(n) space."""
    stack = []
    for a in asteroids:
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
    return stack
