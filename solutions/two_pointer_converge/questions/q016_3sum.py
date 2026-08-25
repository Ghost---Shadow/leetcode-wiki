"""Reshaper for questions/q016_3sum.

Converts this question's (nums) -> list[list[int]] I/O into a call to
the shared converge(): for each fixed index i (after sorting and
skipping duplicate anchors), the inner two-pointer scan over the
remaining sorted range nums[i+1 .. n-1] is one call to converge(), with
step finding pairs summing to -nums[i] and skipping duplicate values via
the closure.
"""
from .. import algorithm as _algorithm
converge = _algorithm.converge


def solve(nums):
    nums = sorted(nums)
    n = len(nums)
    result = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] > 0:
            break

        target = -nums[i]

        def step(left, right, target=target):
            total = nums[left] + nums[right]
            if total < target:
                return (left + 1, right)
            if total > target:
                return (left, right - 1)
            result.append([nums[i], nums[left], nums[right]])
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
            return (left, right)

        converge(i + 1, n - 1, step)

    return result
