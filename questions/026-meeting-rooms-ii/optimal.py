import heapq


def solve(intervals):
    """Optimal: sort meetings by start time and use a min-heap of active end
    times. For each meeting, if the earliest-ending room is free (its end
    time <= current start), reuse it (pop+push); otherwise allocate a new
    room (push). The heap size at any point is the number of rooms needed.
    O(n log n) time, O(n) space."""
    if not intervals:
        return 0

    intervals = sorted(intervals, key=lambda iv: iv[0])
    heap = []  # min-heap of end times of currently occupied rooms

    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heapreplace(heap, end)
        else:
            heapq.heappush(heap, end)

    return len(heap)
