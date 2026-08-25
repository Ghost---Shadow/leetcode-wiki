def solve(s):
    """Brute-force: repeatedly finds the innermost parenthesized group, evaluates
    it with a simple left-to-right +/- reduction, and substitutes the result back
    into the string before rescanning from the top, O(n^2) overall, instead of a
    single O(n) pass with an explicit sign/result stack."""

    def eval_simple(expr):
        # Handles runs of consecutive sign characters (e.g. "--" from substituting
        # a negative inner result) by multiplying signs together rather than
        # just taking the last one.
        expr = expr.replace(' ', '')
        total = 0
        pending_sign = 1
        num = ''
        for ch in expr:
            if ch.isdigit():
                num += ch
            else:
                if num:
                    total += pending_sign * int(num)
                    num = ''
                    pending_sign = 1 if ch == '+' else -1
                else:
                    pending_sign *= 1 if ch == '+' else -1
        if num:
            total += pending_sign * int(num)
        return total

    while '(' in s:
        close = s.index(')')
        open_ = s.rindex('(', 0, close)
        inner_val = eval_simple(s[open_ + 1:close])
        s = s[:open_] + str(inner_val) + s[close + 1:]

    return eval_simple(s)
