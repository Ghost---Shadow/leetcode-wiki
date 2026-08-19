def solve(s):
    """Optimal: single left-to-right pass with an explicit stack for signs
    across parenthesis boundaries. `result` accumulates the running total,
    `sign` is the sign to apply to the next number, and pushing/popping
    (result, sign) onto the stack handles nested parens in O(1) per char.
    O(n) time, O(n) worst-case space for the stack (vs. O(n^2) from repeatedly
    rescanning for parens)."""
    stack = []
    result = 0
    number = 0
    sign = 1

    for ch in s:
        if ch.isdigit():
            number = number * 10 + int(ch)
        elif ch == '+':
            result += sign * number
            number = 0
            sign = 1
        elif ch == '-':
            result += sign * number
            number = 0
            sign = -1
        elif ch == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif ch == ')':
            result += sign * number
            number = 0
            prev_sign = stack.pop()
            prev_result = stack.pop()
            result = prev_result + prev_sign * result

    result += sign * number
    return result
