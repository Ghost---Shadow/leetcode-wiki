import random


def solve(nums, k):
    """Optimal: quickselect. Find the (n-k)-th smallest element (0-indexed)
    using randomized partitioning, which finishes in O(n) expected time and
    O(1) extra space (in-place on a working copy), versus O(n log n) for a
    full sort."""
    nums = list(nums)
    n = len(nums)
    target = n - k  # index of the k-th largest in sorted-ascending order

    def partition(lo, hi, pivot_index):
        pivot_value = nums[pivot_index]
        nums[pivot_index], nums[hi] = nums[hi], nums[pivot_index]
        store_index = lo
        for i in range(lo, hi):
            if nums[i] < pivot_value:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        nums[store_index], nums[hi] = nums[hi], nums[store_index]
        return store_index

    lo, hi = 0, n - 1
    while lo < hi:
        pivot_index = random.randint(lo, hi)
        pivot_index = partition(lo, hi, pivot_index)
        if pivot_index == target:
            break
        elif pivot_index < target:
            lo = pivot_index + 1
        else:
            hi = pivot_index - 1

    return nums[target]
