def solve(s):
    """Brute-force: repeatedly find the innermost bracket pair with a regex
    scan over the whole string and expand it, instead of a single-pass stack.
    O(n^2) or worse due to repeated re-scanning."""
    import re
    pattern = re.compile(r"(\d+)\[([a-zA-Z]*)\]")
    while True:
        match = pattern.search(s)
        if not match:
            break
        count = int(match.group(1))
        inner = match.group(2)
        s = s[:match.start()] + inner * count + s[match.end():]
    return s
