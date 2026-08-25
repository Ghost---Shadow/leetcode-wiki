"""Reshaper for questions/q024_subarray_sum_equals_k.

Converts this question's (nums, k) -> int I/O into a call to the shared
running_fold_sum(): state carries (running prefix sum, counts of prefix
sums seen so far); each step's contribution is the number of earlier
prefixes equal to prefix - k, i.e. the count of subarrays ending here that
sum to k.
"""
from .. import algorithm as _algorithm
running_fold_sum = _algorithm.running_fold_sum


def solve(nums, k):
    def step(state, num):
        prefix, counts = state
        prefix += num
        contribution = counts.get(prefix - k, 0)
        counts[prefix] = counts.get(prefix, 0) + 1
        return (prefix, counts), contribution

    return running_fold_sum(nums, init_state=(0, {0: 1}), step=step)
