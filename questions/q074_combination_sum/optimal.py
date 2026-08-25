def solve(candidates, target):
    """Optimal: backtracking with pruning. Sort candidates, then at each
    step only try candidates >= the last one used (to avoid duplicate
    combinations) and stop as soon as the running sum would exceed target
    (since candidates are sorted, all later ones are even larger). This is
    the standard optimal approach for combination sum."""
    if not candidates:
        return []
    candidates = sorted(candidates)
    results = []
    path = []

    def backtrack(start, remaining):
        if remaining == 0:
            results.append(path[:])
            return
        for i in range(start, len(candidates)):
            c = candidates[i]
            if c > remaining:
                break
            path.append(c)
            backtrack(i, remaining - c)
            path.pop()

    backtrack(0, target)
    return results
