def solve(nums):
    """Brute-force: check every triple of indices for a zero sum. O(n^3),
    deduplicating triplets via a set instead of the sorted two-pointer scan."""
    n = len(nums)
    triplets = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets.add(tuple(sorted((nums[i], nums[j], nums[k]))))
    return [list(t) for t in triplets]
