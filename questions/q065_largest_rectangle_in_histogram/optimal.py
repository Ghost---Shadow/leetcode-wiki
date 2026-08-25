def solve(heights):
    """Optimal: monotonic increasing stack of bar indices. When a shorter
    bar is seen, pop and finalize rectangles for taller bars using the
    current index (and the new stack top) as boundaries. O(n) time,
    O(n) space."""
    stack = []
    best = 0
    n = len(heights)

    for i in range(n + 1):
        h = heights[i] if i < n else 0
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            best = max(best, height * width)
        stack.append(i)

    return best
