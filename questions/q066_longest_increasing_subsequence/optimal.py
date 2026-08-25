import bisect


def solve(nums):
    """Optimal: patience-sorting approach. Maintain `tails`, where tails[k]
    is the smallest possible tail value of an increasing subsequence of
    length k + 1. Binary search each new value's insertion point.
    O(n log n) time, O(n) space."""
    tails = []
    for num in nums:
        idx = bisect.bisect_left(tails, num)
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
    return len(tails)
