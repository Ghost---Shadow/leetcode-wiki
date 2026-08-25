"""Reshaper for questions/q030_move_zeroes.

Converts this question's (nums) -> list[int] I/O into a call to the
shared scan_compact(): each step consumes exactly one element, swapping
it into the write position when nonzero, and always advances read by 1.
"""
from .. import algorithm as _algorithm
scan_compact = _algorithm.scan_compact


def solve(nums):
    nums = list(nums)

    def step(read, write):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
        return read + 1, write

    scan_compact(len(nums), step)
    return nums
