def solve(nums1, m, nums2, n):
    """Optimal: two-pointer merge from the back. Since nums1 has trailing empty
    slots, fill it from the end, always placing the larger of the two current
    tail candidates -- O(m + n) time, O(1) extra space (writes directly into
    nums1's existing slots)."""
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    return nums1
