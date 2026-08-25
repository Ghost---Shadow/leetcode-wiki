from collections import Counter


def solve(s, t):
    """Optimal: sliding window with two pointers. Expand the right edge until the
    window satisfies all character counts of t, then contract the left edge as
    much as possible while still satisfying it, tracking the best window seen --
    O(n) time, O(k) space where k is the number of distinct characters in t."""
    if not s or not t:
        return ""

    need = Counter(t)
    missing = len(t)

    best_len = float("inf")
    best_start = 0
    left = 0

    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1

        while missing == 0:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_start = left
            left_ch = s[left]
            need[left_ch] += 1
            if need[left_ch] > 0:
                missing += 1
            left += 1

    if best_len == float("inf"):
        return ""
    return s[best_start:best_start + best_len]
