def solve(strs):
    """Brute-force: try the entire first string as the prefix, then shrink it
    by one character at a time until every string starts with it. O(n*m^2)."""
    if not strs:
        return ""
    prefix = strs[0]
    while prefix:
        if all(s.startswith(prefix) for s in strs):
            return prefix
        prefix = prefix[:-1]
    return ""
