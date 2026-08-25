def solve(nums):
    """Optimal: greedy scan tracking the farthest index reachable so far.
    O(n) time, O(1) space."""
    farthest = 0
    for i, step in enumerate(nums):
        if i > farthest:
            return False
        if i + step > farthest:
            farthest = i + step
    return True
