def solve(num_courses, prerequisites):
    """Brute-force: repeatedly scan the full prerequisite list, removing any
    course whose prerequisites are all satisfied, until no more progress can
    be made. If every course gets removed, there's no cycle. O(V*E) instead
    of a single-pass topological sort / DFS cycle check."""
    remaining = set(range(num_courses))
    prereqs = [tuple(p) for p in prerequisites]

    progress = True
    while progress and remaining:
        progress = False
        for course in list(remaining):
            needs = [p[1] for p in prereqs if p[0] == course and p[1] in remaining]
            if not needs:
                remaining.discard(course)
                progress = True

    return len(remaining) == 0
