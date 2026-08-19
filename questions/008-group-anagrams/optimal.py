from collections import defaultdict


def solve(strs):
    """Optimal: hash map keyed by per-string character counts. O(n * k) time
    (n strings, average length k), O(n * k) space -- avoids the O(k log k)
    sort-per-string used by the sorted-string-key approach."""
    groups = defaultdict(list)
    for s in strs:
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord("a")] += 1
        groups[tuple(counts)].append(s)
    return list(groups.values())
