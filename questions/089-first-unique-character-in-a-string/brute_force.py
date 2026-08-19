def solve(s):
    """Brute-force: for each character, rescans the entire string to count
    occurrences, O(n^2), instead of a single O(n) pass with a hash map."""
    n = len(s)
    for i in range(n):
        count = 0
        for j in range(n):
            if s[j] == s[i]:
                count += 1
        if count == 1:
            return i
    return -1
