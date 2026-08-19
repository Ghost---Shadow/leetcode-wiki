from collections import deque


def solve(num_courses, prerequisites):
    """Kahn's algorithm (BFS topological sort): compute in-degrees, repeatedly
    remove zero-in-degree nodes and decrement their neighbors' in-degrees.
    All courses can be finished iff every node gets removed, i.e. no cycle
    exists. O(V + E) time, O(V + E) space."""
    graph = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses

    for course, pre in prerequisites:
        graph[pre].append(course)
        in_degree[course] += 1

    queue = deque(c for c in range(num_courses) if in_degree[c] == 0)
    visited = 0

    while queue:
        node = queue.popleft()
        visited += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return visited == num_courses
