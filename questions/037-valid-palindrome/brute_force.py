def solve(s):
    """Brute-force: build a fully cleaned copy of the string, then build its
    reverse by re-scanning from the end each time (O(n) work per character
    instead of O(1) index access), giving O(n^2) overall."""
    cleaned = [ch.lower() for ch in s if ch.isalnum()]
    n = len(cleaned)
    for i in range(n):
        mirror = cleaned[n - 1 - i]
        if cleaned[i] != mirror:
            return False
    return True
