def solve(s):
    """Optimal: single left-to-right pass. Add each symbol's value, but if it is
    smaller than the value that follows it, subtract instead of add -- O(n) time,
    O(1) space."""
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    n = len(s)
    for i in range(n):
        cur = values[s[i]]
        if i + 1 < n and cur < values[s[i + 1]]:
            total -= cur
        else:
            total += cur
    return total
