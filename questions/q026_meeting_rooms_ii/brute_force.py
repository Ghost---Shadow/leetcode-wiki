def solve(intervals):
    """Brute-force: for every minute in the overall range, count how many
    meetings are active and track the max, instead of a sweep-line over sorted
    start/end events. O(n * range)."""
    if not intervals:
        return 0
    max_time = max(end for _, end in intervals)
    max_rooms = 0
    for t in range(max_time + 1):
        count = 0
        for start, end in intervals:
            if start <= t < end:
                count += 1
        max_rooms = max(max_rooms, count)
    return max_rooms
