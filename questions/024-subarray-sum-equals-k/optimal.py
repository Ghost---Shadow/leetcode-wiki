def solve(nums, k):
    """Prefix sum + hash map: track how many times each prefix sum has
    occurred; a subarray (i, j] sums to k exactly when
    prefix[j] - prefix[i] == k, so look up prefix[j] - k in the map.
    O(n) time, O(n) space."""
    counts = {0: 1}
    prefix = 0
    result = 0
    for num in nums:
        prefix += num
        result += counts.get(prefix - k, 0)
        counts[prefix] = counts.get(prefix, 0) + 1
    return result
