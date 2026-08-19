def solve(nums, k):
    """Brute-force: sort the whole array and index from the end,
    instead of quickselect/heap-based O(n) or O(n log k)."""
    return sorted(nums)[-k]
