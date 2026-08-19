def solve(s):
    """Optimal: single-pass stack-based decoding. Push (current_string,
    repeat_count) whenever a '[' is opened, and pop/combine on ']'. Each
    character is processed a constant number of times overall. O(n) time
    (n = length of decoded output in the worst case), O(n) space."""
    stack = []
    current = ""
    num = 0

    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == "[":
            stack.append((current, num))
            current = ""
            num = 0
        elif ch == "]":
            prev_string, count = stack.pop()
            current = prev_string + current * count
        else:
            current += ch

    return current
