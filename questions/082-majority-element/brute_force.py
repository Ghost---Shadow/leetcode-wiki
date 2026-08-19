def solve(nums):
    """Brute-force: for every distinct candidate value, count its occurrences
    with a full scan of the array. O(n^2) instead of the O(n) Boyer-Moore
    majority vote algorithm."""
    n = len(nums)
    for candidate in set(nums):
        count = sum(1 for x in nums if x == candidate)
        if count > n // 2:
            return candidate
    return None
