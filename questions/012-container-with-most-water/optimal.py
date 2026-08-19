def solve(height):
    """Two pointers starting at both ends, always moving the shorter line
    inward (moving the taller one can never improve the area). O(n) time,
    O(1) space."""
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        h = min(height[left], height[right])
        best = max(best, (right - left) * h)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best
