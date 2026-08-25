from collections import defaultdict


def solve(equations, values, queries):
    """Brute-force: builds a weighted graph, then for every query runs a fresh DFS
    over the whole graph from scratch, instead of a union-find with weighted path
    compression that answers each query near O(1)."""
    graph = defaultdict(dict)
    for (a, b), v in zip(equations, values):
        graph[a][b] = v
        graph[b][a] = 1.0 / v

    def dfs(src, dst, visited):
        if src not in graph or dst not in graph:
            return -1.0
        if src == dst:
            return 1.0
        visited.add(src)
        for neighbor, weight in graph[src].items():
            if neighbor in visited:
                continue
            result = dfs(neighbor, dst, visited)
            if result != -1.0:
                return weight * result
        return -1.0

    results = []
    for a, b in queries:
        results.append(dfs(a, b, set()))
    return results
