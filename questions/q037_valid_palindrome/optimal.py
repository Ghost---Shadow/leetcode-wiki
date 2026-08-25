def solve(s):
    """Optimal: two pointers converging from both ends of the original
    string, skipping non-alphanumeric characters in place, with no auxiliary
    cleaned copy built up front. O(n) time, O(1) extra space."""
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True
