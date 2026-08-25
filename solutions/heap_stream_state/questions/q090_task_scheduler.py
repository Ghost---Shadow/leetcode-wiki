"""Reshaper for questions/q090_task_scheduler.

Converts this question's (tasks, n) -> int I/O into a call to the shared
schedule_with_cooldown(): only the per-task frequency counts and the
cooldown length matter, not the task labels themselves.
"""
from collections import Counter

from .. import algorithm as _algorithm
schedule_with_cooldown = _algorithm.schedule_with_cooldown


def solve(tasks, n):
    counts = Counter(tasks).values()
    return schedule_with_cooldown(counts, n)
