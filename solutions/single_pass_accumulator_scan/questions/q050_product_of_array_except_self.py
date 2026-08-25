"""Reshaper for questions/q050_product_of_array_except_self.

Converts this question's (nums,) -> list[int] I/O into two calls to the
shared scan(): a left-to-right pass writing running prefix products into
`result`, then a right-to-left pass multiplying in a running suffix
product. No division used.
"""
from .. import algorithm as _algorithm
scan = _algorithm.scan


def solve(nums):
    n = len(nums)
    result = [1] * n

    def prefix_combine(prefix, i):
        result[i] = prefix
        return prefix * nums[i]

    scan(list(range(n)), 1, prefix_combine)

    def suffix_combine(suffix, i):
        result[i] *= suffix
        return suffix * nums[i]

    scan(list(range(n - 1, -1, -1)), 1, suffix_combine)

    return result
