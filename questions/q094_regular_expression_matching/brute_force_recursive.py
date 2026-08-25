def solve(s, p):
    """Brute-force recursion without memoization: at every '*' it explores both
    the zero-occurrence and the consume-one-and-retry branches from scratch,
    exponential time in the worst case, instead of the O(n*m) DP."""
    if not p:
        return not s

    first_match = bool(s) and p[0] in (s[0], '.')

    if len(p) >= 2 and p[1] == '*':
        return solve(s, p[2:]) or (first_match and solve(s[1:], p))

    return first_match and solve(s[1:], p[1:])
