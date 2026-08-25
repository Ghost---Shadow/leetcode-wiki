def solve(strs):
    """Brute-force: pairwise-compare sorted characters of every string
    instead of hashing each string's signature. O(n^2 * k log k)."""
    n = len(strs)
    used = [False] * n
    groups = []
    for i in range(n):
        if used[i]:
            continue
        group = [strs[i]]
        used[i] = True
        for j in range(i + 1, n):
            if not used[j] and sorted(strs[i]) == sorted(strs[j]):
                group.append(strs[j])
                used[j] = True
        groups.append(group)
    return groups
