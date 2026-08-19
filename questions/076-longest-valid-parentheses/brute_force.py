def solve(s):
    """Brute-force: check every substring for whether it forms a valid
    parenthesization. O(n^3): O(n^2) substrings, each validated in O(n)."""
    n = len(s)

    def is_valid(sub):
        balance = 0
        for ch in sub:
            if ch == "(":
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    best = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if is_valid(s[i:j]):
                best = max(best, j - i)
    return best
