def solve(s):
    """Optimal: single left-to-right pass tracking the previous operator
    and the current number. On '+'/'-' push the signed value; on '*'/'/'
    fold immediately into the last pushed value. O(n) time, O(n) space for
    the running stack of terms (O(1) extra beyond the output accumulation)."""
    stack = []
    num = 0
    op = "+"
    n = len(s)

    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num * 10 + int(ch)
        if (not ch.isspace() and not ch.isdigit()) or i == n - 1:
            if op == "+":
                stack.append(num)
            elif op == "-":
                stack.append(-num)
            elif op == "*":
                stack.append(stack.pop() * num)
            elif op == "/":
                prev = stack.pop()
                stack.append(int(prev / num))
            op = ch
            num = 0

    return sum(stack)
