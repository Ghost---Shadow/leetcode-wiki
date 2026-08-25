"""Reshaper for questions/q096_maximum_profit_in_job_scheduling.

Converts this question's (startTime, endTime, profit) -> int I/O into a
call to the shared sweep_sorted(): sort jobs by end time, then fold a
"(dp table, end-times-seen list)" state -- for each job, binary search the
end-times seen so far for the last job compatible with this one's start,
and take the max of skipping vs taking this job.
"""
import bisect

from .. import algorithm as _algorithm
sweep_sorted = _algorithm.sweep_sorted


def solve(startTime, endTime, profit):
    jobs = list(zip(startTime, endTime, profit))

    def step(state, job):
        dp, ends = state
        start, end, p = job
        k = bisect.bisect_right(ends, start)
        dp.append(max(dp[-1], dp[k] + p))
        ends.append(end)
        return (dp, ends)

    dp, _ = sweep_sorted(jobs, key=lambda j: j[1], init_state=([0], []), step=step)
    return dp[-1]
