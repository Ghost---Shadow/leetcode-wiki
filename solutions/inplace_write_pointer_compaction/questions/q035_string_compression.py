"""Reshaper for questions/q035_string_compression.

Converts this question's (chars) -> int I/O (in-place mutation, returns
new length) into a call to the shared scan_compact(): each step consumes
a whole run of equal characters starting at `read`, writing the
character and (if the run is longer than 1) each digit of its length.
"""
from .. import algorithm as _algorithm
scan_compact = _algorithm.scan_compact


def solve(chars):
    n = len(chars)

    def step(read, write):
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

        return read, write

    new_len = scan_compact(n, step)
    del chars[new_len:]
    return new_len
