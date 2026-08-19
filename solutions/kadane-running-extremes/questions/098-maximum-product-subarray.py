"""Reshaper for questions/098-maximum-product-subarray.

Converts this question's (nums) -> int I/O into a call to the shared
running_fold_best(), where state is (running max, running min) ending here
-- tracking the min too because a negative running min times a new negative
number can become the new running max.
"""
import importlib.util
import os

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("algorithm", os.path.join(_here, "..", "algorithm.py"))
_algorithm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_algorithm)
running_fold_best = _algorithm.running_fold_best


def _step(state, v):
    cur_max, cur_min = state
    candidates = (v, cur_max * v, cur_min * v)
    return (max(candidates), min(candidates))


def solve(nums):
    return running_fold_best(
        nums,
        init_state=lambda v: (v, v),
        step=_step,
        extract=lambda state: state[0],
    )
