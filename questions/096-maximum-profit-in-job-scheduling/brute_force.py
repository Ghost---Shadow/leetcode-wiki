def solve(startTime, endTime, profit):
    """Brute-force: enumerates all 2^n subsets of jobs, keeps the subsets with no
    pairwise time overlap, and returns the best total profit among them, instead
    of sorting by end time and using DP with binary search."""
    n = len(startTime)
    jobs = list(zip(startTime, endTime, profit))
    best = 0

    for mask in range(1 << n):
        chosen = [jobs[i] for i in range(n) if mask & (1 << i)]
        valid = True
        for a in range(len(chosen)):
            for b in range(a + 1, len(chosen)):
                s1, e1, _ = chosen[a]
                s2, e2, _ = chosen[b]
                if s1 < e2 and s2 < e1:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            total = sum(p for _, _, p in chosen)
            best = max(best, total)

    return best
