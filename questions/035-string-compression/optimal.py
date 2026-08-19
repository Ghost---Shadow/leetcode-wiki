def solve(chars):
    """Optimal: single in-place two-pointer pass. `write` marks where the
    next compressed character/digits go; `read` scans forward counting the
    current run before writing the character and (if run > 1) each digit of
    its length. O(n) time, O(1) extra space."""
    n = len(chars)
    write = 0
    read = 0

    while read < n:
        char = chars[read]
        run_length = 0
        while read < n and chars[read] == char:
            read += 1
            run_length += 1

        chars[write] = char
        write += 1

        if run_length > 1:
            for digit in str(run_length):
                chars[write] = digit
                write += 1

    del chars[write:]
    return write
