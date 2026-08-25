def solve(nums, target):
    """Brute-force: linearly scan the whole array tracking the first and
    last matching index, O(n) instead of two O(log n) binary searches."""
    first = -1
    last = -1
    for i, v in enumerate(nums):
        if v == target:
            if first == -1:
                first = i
            last = i
    return [first, last]
