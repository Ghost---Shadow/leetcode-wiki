def solve(nums, k):
    """Brute-force: count frequencies, then repeatedly scan the whole
    frequency table k times to pull out the current max. O(n * k)."""
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    remaining = dict(counts)
    result = []
    for _ in range(k):
        best_num = max(remaining, key=lambda num: remaining[num])
        result.append(best_num)
        del remaining[best_num]
    return result
