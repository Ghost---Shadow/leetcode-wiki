"""Reshaper for questions/q011_maximum_subarray.

Converts this question's (nums) -> int I/O into a call to the shared
running_fold_best(), where state is just the running max-ending-here.
"""
from .. import algorithm as _algorithm
running_fold_best = _algorithm.running_fold_best


def solve(nums):
    return running_fold_best(
        nums,
        init_state=lambda v: v,
        step=lambda cur, v: max(v, cur + v),
        extract=lambda cur: cur,
    )
