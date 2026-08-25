def solve(nums1, nums2):
    """Brute-force: merge both arrays with a full sort, then read off the
    median directly. O((m+n) log(m+n)) instead of the O(log(min(m,n)))
    binary-search partition approach."""
    merged = sorted(nums1 + nums2)
    n = len(merged)
    mid = n // 2
    if n % 2 == 1:
        return float(merged[mid])
    return (merged[mid - 1] + merged[mid]) / 2.0
