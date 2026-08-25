def solve(s):
    """Optimal: two-pass counter method. Scan left-to-right tracking counts
    of '(' and ')'; whenever they're equal, record a valid length, and
    whenever ')' exceeds '(', reset both counters (invalid segment). Then
    scan right-to-left symmetrically to catch cases like "(()" where '('
    is never fully balanced from the left. O(n) time, O(1) space."""
    best = 0
    left = right = 0
    for ch in s:
        if ch == "(":
            left += 1
        else:
            right += 1
        if left == right:
            best = max(best, 2 * right)
        elif right > left:
            left = right = 0

    left = right = 0
    for ch in reversed(s):
        if ch == "(":
            left += 1
        else:
            right += 1
        if left == right:
            best = max(best, 2 * left)
        elif left > right:
            left = right = 0

    return best
