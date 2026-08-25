from itertools import permutations


def solve(nums):
    """Brute-force: generate every distinct permutation of nums, sort them
    all lexicographically, and return the one right after the current
    arrangement (wrapping to the smallest if already the last). O(n! log n!)
    instead of the O(n) in-place pivot/swap/reverse approach."""
    perms = sorted(set(permutations(nums)))
    cur = tuple(nums)
    idx = perms.index(cur)
    if idx == len(perms) - 1:
        return list(perms[0])
    return list(perms[idx + 1])
