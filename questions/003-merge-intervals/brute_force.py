def solve(intervals):
    """Brute-force: repeatedly scan for any overlapping pair and merge it,
    instead of sorting once and sweeping left-to-right."""
    intervals = [list(iv) for iv in intervals]
    merged_any = True
    while merged_any:
        merged_any = False
        result = []
        while intervals:
            cur = intervals.pop()
            merged_this = False
            for other in result:
                if cur[0] <= other[1] and other[0] <= cur[1]:
                    other[0] = min(other[0], cur[0])
                    other[1] = max(other[1], cur[1])
                    merged_this = True
                    merged_any = True
                    break
            if not merged_this:
                result.append(cur)
        intervals = result
    return sorted(intervals)
