def solve(nums):
    """Brute-force: for every number, repeatedly probe num+1, num+2, ... via
    linear `in` lookups on the list, instead of using a hash set for O(1)
    membership checks. O(n^3) worst case."""
    best = 0
    for num in nums:
        length = 1
        current = num
        while (current + 1) in nums:
            current += 1
            length += 1
        best = max(best, length)
    return best
