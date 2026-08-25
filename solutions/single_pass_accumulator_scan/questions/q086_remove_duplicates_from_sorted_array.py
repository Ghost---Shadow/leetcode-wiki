"""Reshaper for questions/q086_remove_duplicates_from_sorted_array.

Converts this question's (nums,) -> list[int] I/O into a call to the
shared scan(): items are nums[1:], the accumulator is the write pointer,
and combine() writes each item into its slot in place whenever it differs
from the last kept element.
"""
from .. import algorithm as _algorithm
scan = _algorithm.scan


def solve(nums):
    nums = list(nums)
    if not nums:
        return []

    def combine(write, x):
        if x != nums[write - 1]:
            nums[write] = x
            return write + 1
        return write

    write = scan(nums[1:], 1, combine)
    return nums[:write]
