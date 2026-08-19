def solve(n):
    """Optimal: Floyd's cycle detection (fast/slow pointer) over the
    sequence of digit-square sums. Detects a cycle in O(1) extra space
    instead of a hash set that grows with the cycle length."""

    def next_number(x):
        total = 0
        while x > 0:
            digit = x % 10
            total += digit * digit
            x //= 10
        return total

    slow = n
    fast = next_number(n)
    while fast != 1 and slow != fast:
        slow = next_number(slow)
        fast = next_number(next_number(fast))

    return fast == 1
