from collections import deque


def kahn_topological_order(num_nodes, edges):
    """Kahn's BFS topological sort over a directed graph with `num_nodes`
    nodes (0..num_nodes-1) and `edges` as (u, v) pairs meaning u -> v.

    Returns a list of all nodes in topological order, or None if the graph
    has a cycle (fewer than num_nodes nodes could be ordered). O(V + E).
    """
    adjacency = [[] for _ in range(num_nodes)]
    indegree = [0] * num_nodes
    for u, v in edges:
        adjacency[u].append(v)
        indegree[v] += 1

    queue = deque(i for i in range(num_nodes) if indegree[i] == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in adjacency[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    return order if len(order) == num_nodes else None
