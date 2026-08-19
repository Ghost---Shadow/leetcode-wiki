def solve(nums, k):
    """Bucket sort by frequency: index buckets 0..n by count, then walk
    from the highest-frequency bucket down, collecting elements. O(n)
    time, O(n) space (avoids an O(n log n) sort of the frequency table)."""
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    n = len(nums)
    buckets = [[] for _ in range(n + 1)]
    for num, freq in counts.items():
        buckets[freq].append(num)

    result = []
    for freq in range(n, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result
