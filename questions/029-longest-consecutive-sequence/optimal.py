def solve(nums):
    """Optimal: put all numbers in a hash set, then only start counting a
    sequence from numbers that are the start of a run (i.e. num - 1 is not
    in the set). Each number is visited at most twice overall, giving O(n)
    time and O(n) space."""
    num_set = set(nums)
    best = 0

    for num in num_set:
        if (num - 1) not in num_set:
            current = num
            length = 1
            while (current + 1) in num_set:
                current += 1
                length += 1
            best = max(best, length)

    return best
