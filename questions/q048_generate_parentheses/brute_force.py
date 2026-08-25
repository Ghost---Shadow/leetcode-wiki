from itertools import product


def solve(n):
    """Brute-force: generates all 2^(2n) strings of '(' and ')' of length 2n via
    itertools.product, then filters for validity -- instead of only constructing
    valid sequences directly via backtracking with pruning."""
    if n == 0:
        return [""]

    results = []
    for combo in product("()", repeat=2 * n):
        s = "".join(combo)
        balance = 0
        valid = True
        for ch in s:
            balance += 1 if ch == "(" else -1
            if balance < 0:
                valid = False
                break
        if valid and balance == 0:
            results.append(s)
    return results
