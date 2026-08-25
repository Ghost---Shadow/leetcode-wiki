def solve(nums1, m, nums2, n):
    """Brute-force: concatenates the first m elements of nums1 with the first n
    elements of nums2 and sorts the combined list -- O((m+n) log(m+n)) instead of
    the O(m+n) two-pointer merge from the back."""
    merged = nums1[:m] + nums2[:n]
    merged.sort()
    return merged
