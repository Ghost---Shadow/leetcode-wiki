def solve(numCourses, prerequisites):
    """Brute-force topological sort: on every step, rescans *all* remaining courses
    from scratch looking for one whose prerequisites are already satisfied, instead
    of maintaining a queue of zero-in-degree nodes (Kahn's algorithm) -- O(V*(V+E))
    instead of O(V+E)."""
    remaining = set(range(numCourses))
    deps = {c: set() for c in range(numCourses)}
    for course, pre in prerequisites:
        deps[course].add(pre)

    order = []
    while remaining:
        found = None
        for c in sorted(remaining):
            if deps[c] & remaining:
                continue
            found = c
            break
        if found is None:
            return []
        order.append(found)
        remaining.remove(found)
    return order
