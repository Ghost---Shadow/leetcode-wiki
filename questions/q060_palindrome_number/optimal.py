def solve(x):
    """Optimal: reverse only the second half of the number and compare it
    against the remaining first half, avoiding overflow concerns and doing
    half the work. O(log n) time, O(1) space, no string conversion."""
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reverted = 0
    while x > reverted:
        reverted = reverted * 10 + x % 10
        x //= 10

    return x == reverted or x == reverted // 10
