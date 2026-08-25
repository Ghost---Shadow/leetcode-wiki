import bisect


def solve(startTime, endTime, profit):
    """Optimal: sort jobs by end time, then DP where dp[i] is the best profit
    using a prefix of the sorted jobs. For each job, binary search (bisect) for
    the last job whose end time is <= this job's start time, so we either skip
    the job or take it plus the best profit of jobs compatible with it.
    O(n log n) time, O(n) space, versus the brute force's O(2^n) subset
    enumeration."""
    n = len(startTime)
    jobs = sorted(zip(endTime, startTime, profit))
    ends = [job[0] for job in jobs]

    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        end, start, p = jobs[i - 1]
        # last index (0-based, in dp terms 1-based) with end <= start
        k = bisect.bisect_right(ends, start, 0, i - 1)
        dp[i] = max(dp[i - 1], dp[k] + p)

    return dp[n]
