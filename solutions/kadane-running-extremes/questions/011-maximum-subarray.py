"""Reshaper for questions/011-maximum-subarray.

Converts this question's (nums) -> int I/O into a call to the shared
running_fold_best(), where state is just the running max-ending-here.
"""
import importlib.util
import os

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("algorithm", os.path.join(_here, "..", "algorithm.py"))
_algorithm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_algorithm)
running_fold_best = _algorithm.running_fold_best


def solve(nums):
    return running_fold_best(
        nums,
        init_state=lambda v: v,
        step=lambda cur, v: max(v, cur + v),
        extract=lambda cur: cur,
    )
