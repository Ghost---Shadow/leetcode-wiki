"""Heap-backed running state maintained across an open-ended sequence of
operations, rather than a fixed graph unfolded once.

Both routines here are standalone (not built on _meta explore()): there is
no static state graph to unfold, just a persistent structure -- a pair of
balanced heaps, or a heap plus a cooldown queue -- updated one arrival (or
one time slot) at a time. This is exactly the kind of "known outlier" the
"combine"/union-find/in-place-partitioning note in solutions/README.md
anticipates: still a heap technique in spirit, just not an instantiation of
the shared explore() engine.
"""
import heapq
from collections import deque


class TwoHeapMedian:
    """Maintains the running median of a stream of numbers using a
    max-heap (values negated) for the lower half and a min-heap for the
    upper half, kept balanced in size so the median is always at (one of)
    the tops. push() is O(log n); median() is O(1).
    """

    def __init__(self):
        self._lo = []  # max-heap (store negated values): lower half
        self._hi = []  # min-heap: upper half

    def push(self, num):
        heapq.heappush(self._lo, -num)
        heapq.heappush(self._hi, -heapq.heappop(self._lo))
        if len(self._hi) > len(self._lo):
            heapq.heappush(self._lo, -heapq.heappop(self._hi))

    def median(self):
        if len(self._lo) > len(self._hi):
            return float(-self._lo[0])
        return (-self._lo[0] + self._hi[0]) / 2.0


def schedule_with_cooldown(counts, cooldown):
    """Given task frequency `counts` (an iterable of per-task counts) and a
    required `cooldown` number of slots between two runs of the same task,
    returns the minimum number of time slots needed to run every task at
    least once: greedily always run whichever remaining task currently has
    the highest count, sending it to a cooldown queue until it is runnable
    again, and refilling the heap from that queue as tasks come off
    cooldown. O(total tasks) time.
    """
    heap = [-c for c in counts if c > 0]
    heapq.heapify(heap)
    pending = deque()  # (release_time, remaining_count) waiting out cooldown

    time = 0
    while heap or pending:
        time += 1
        if heap:
            remaining = -heapq.heappop(heap) - 1
            if remaining > 0:
                pending.append((time + cooldown, remaining))
        if pending and pending[0][0] == time:
            heapq.heappush(heap, -pending.popleft()[1])
        if not heap and pending:
            time = pending[0][0] - 1

    return time
