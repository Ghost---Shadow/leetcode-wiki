from collections import deque


def solve(numCourses, prerequisites):
    """Optimal: Kahn's algorithm (BFS topological sort). Build an adjacency list
    and in-degree count, seed a queue with all zero-in-degree nodes, then repeatedly
    pop a node, append it to the order, and decrement its neighbors' in-degrees,
    pushing any that hit zero -- O(V + E) time, O(V + E) space."""
    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for course, pre in prerequisites:
        graph[pre].append(course)
        indegree[course] += 1

    queue = deque(c for c in range(numCourses) if indegree[c] == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    if len(order) != numCourses:
        return []
    return order
