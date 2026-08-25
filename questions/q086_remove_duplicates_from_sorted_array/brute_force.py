def solve(nums):
    """Brute-force dedup: for each element, linearly scans the entire result-so-far
    list to check for duplicates, O(n^2), instead of the O(n) two-pointer scan that
    only ever compares against the last kept element."""
    result = []
    for x in nums:
        if x not in result:
            result.append(x)
    return result
