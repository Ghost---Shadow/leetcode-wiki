"""Reshaper for questions/q026_meeting_rooms_ii.

Converts this question's intervals -> int I/O into a call to the shared
priority_pop_stream(): seed the frontier with every meeting, popped in
start-time order; each pop's transition reuses the earliest-ending room if
it is free by then (otherwise allocates a new one) via a closure-held
min-heap of room end times, tracking the running peak room count as a
side effect. Meetings have no successors of their own.
"""
import heapq

from .. import algorithm as _algorithm
priority_pop_stream = _algorithm.priority_pop_stream


def solve(intervals):
    if not intervals:
        return 0

    room_ends = []  # min-heap of currently occupied rooms' end times
    max_rooms = 0

    def transition(meeting):
        nonlocal max_rooms
        start, end = meeting
        if room_ends and room_ends[0] <= start:
            heapq.heapreplace(room_ends, end)
        else:
            heapq.heappush(room_ends, end)
        max_rooms = max(max_rooms, len(room_ends))
        return ()

    def priority(meeting):
        return meeting[0]

    for _ in priority_pop_stream(intervals, transition, priority):
        pass

    return max_rooms
