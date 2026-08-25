def solve(nums):
    """Optimal: Boyer-Moore voting algorithm. Maintain a candidate and a
    running count; increment when seeing the candidate, decrement
    otherwise, and switch candidates when the count hits zero. The
    majority element (guaranteed to exist, appearing more than n/2 times)
    always survives this process. O(n) time, O(1) space."""
    candidate = None
    count = 0
    for x in nums:
        if count == 0:
            candidate = x
        count += 1 if x == candidate else -1
    return candidate
