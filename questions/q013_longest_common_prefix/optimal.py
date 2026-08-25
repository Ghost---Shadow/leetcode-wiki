def solve(strs):
    """Vertical scanning: compare characters column by column across all
    strings, stopping at the first mismatch or the shortest string's end.
    O(n*m) time (n = number of strings, m = length of shortest string),
    O(1) extra space."""
    if not strs:
        return ""
    for i, ch in enumerate(strs[0]):
        for s in strs[1:]:
            if i >= len(s) or s[i] != ch:
                return strs[0][:i]
    return strs[0]
