def solve(intervals):
    """Optimal: sort by start once, then sweep left-to-right merging overlaps.
    O(n log n) time, O(n) space."""
    if not intervals:
        return []
    intervals = sorted([list(iv) for iv in intervals], key=lambda iv: iv[0])
    result = [intervals[0]]
    for start, end in intervals[1:]:
        last = result[-1]
        if start <= last[1]:
            last[1] = max(last[1], end)
        else:
            result.append([start, end])
    return result
