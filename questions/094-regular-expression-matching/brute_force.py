def solve(s, p):
    """Brute-force, no memoization: explores both the zero-occurrence and the
    consume-one-and-retry branches at every '*' via an explicit stack of
    (remaining s, remaining p) states instead of recursion -- same
    exponential worst case as the recursive version."""
    stack = [(s, p)]
    while stack:
        cur_s, cur_p = stack.pop()
        if not cur_p:
            if not cur_s:
                return True
            continue

        first_match = bool(cur_s) and cur_p[0] in (cur_s[0], ".")

        if len(cur_p) >= 2 and cur_p[1] == "*":
            stack.append((cur_s, cur_p[2:]))
            if first_match:
                stack.append((cur_s[1:], cur_p))
        elif first_match:
            stack.append((cur_s[1:], cur_p[1:]))

    return False
