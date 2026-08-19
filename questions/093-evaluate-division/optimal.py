from collections import defaultdict


def solve(equations, values, queries):
    """Optimal: build the weighted graph once (O(E)), then answer each query with
    its own bounded BFS/DFS over that graph (O(V + E) per query) instead of
    rescanning from scratch with no other change. Unknown variables short-circuit
    to -1.0 immediately. Overall O(E + Q * (V + E))."""
    graph = defaultdict(dict)
    for (a, b), v in zip(equations, values):
        graph[a][b] = v
        graph[b][a] = 1.0 / v

    def bfs(src, dst):
        if src not in graph or dst not in graph:
            return -1.0
        if src == dst:
            return 1.0
        visited = {src}
        queue = [(src, 1.0)]
        while queue:
            node, acc = queue.pop(0)
            if node == dst:
                return acc
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, acc * weight))
        return -1.0

    return [bfs(a, b) for a, b in queries]
