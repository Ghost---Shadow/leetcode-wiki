def solve(n):
    """Brute-force: track every number seen so far in a hash set to detect a
    cycle, using O(cycle length) extra space, instead of the O(1)-space
    Floyd's cycle-detection (fast/slow pointer) approach."""

    def next_number(x):
        total = 0
        while x > 0:
            digit = x % 10
            total += digit * digit
            x //= 10
        return total

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = next_number(n)
    return n == 1
