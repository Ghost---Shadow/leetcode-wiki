def solve(nums):
    """Brute-force: build every permutation by recursively inserting each
    number into every possible position of every partial permutation built
    so far, instead of the standard swap-based in-place backtracking."""
    result = [[]]
    for num in nums:
        new_result = []
        for perm in result:
            for pos in range(len(perm) + 1):
                new_result.append(perm[:pos] + [num] + perm[pos:])
        result = new_result
    return result
