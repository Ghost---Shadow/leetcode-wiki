from collections import defaultdict


def solve(equations, values, queries):
    """Brute-force: builds a weighted graph, then for every query runs a
    fresh DFS over the whole graph from scratch (via an explicit stack
    instead of recursion), instead of a union-find with weighted path
    compression that answers each query near O(1)."""
    graph = defaultdict(dict)
    for (a, b), v in zip(equations, values):
        graph[a][b] = v
        graph[b][a] = 1.0 / v

    def dfs(src, dst):
        if src not in graph or dst not in graph:
            return -1.0
        if src == dst:
            return 1.0
        visited = {src}
        stack = [(src, 1.0)]
        while stack:
            node, product = stack.pop()
            for neighbor, weight in graph[node].items():
                if neighbor in visited:
                    continue
                if neighbor == dst:
                    return product * weight
                visited.add(neighbor)
                stack.append((neighbor, product * weight))
        return -1.0

    results = []
    for a, b in queries:
        results.append(dfs(a, b))
    return results
