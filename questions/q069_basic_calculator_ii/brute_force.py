import re


def solve(s):
    """Brute-force: tokenize the expression, then repeatedly rescan the
    entire token list from the start to resolve one '*' or '/' at a time
    (restarting the scan after each resolution), O(n^2) instead of a single
    O(n) pass that tracks the previous operator."""
    tokens = re.findall(r"\d+|[+\-*/]", s.replace(" ", ""))
    tokens = [int(t) if t not in "+-*/" else t for t in tokens]

    changed = True
    while changed:
        changed = False
        for i, t in enumerate(tokens):
            if t in ("*", "/"):
                a, b = tokens[i - 1], tokens[i + 1]
                val = a * b if t == "*" else int(a / b)
                tokens = tokens[:i - 1] + [val] + tokens[i + 2:]
                changed = True
                break

    result = tokens[0]
    i = 1
    while i < len(tokens):
        op = tokens[i]
        val = tokens[i + 1]
        if op == "+":
            result += val
        else:
            result -= val
        i += 2
    return result
