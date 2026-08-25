"""Reshaper for questions/q093_evaluate_division.

Converts this question's (equations, values, queries) -> list[float] I/O
into repeated calls to the shared multi_source_bfs(): build a weighted graph
from the equations (a/b = v gives edge a->b weight v and b->a weight 1/v),
then for each query BFS out from the source node accumulating the product
of edge weights along the way until the target node is reached.
"""
from collections import defaultdict

from .. import algorithm as _algorithm
multi_source_bfs = _algorithm.multi_source_bfs


def solve(equations, values, queries):
    graph = defaultdict(dict)
    for (a, b), v in zip(equations, values):
        graph[a][b] = v
        graph[b][a] = 1.0 / v

    def answer(src, dst):
        if src not in graph or dst not in graph:
            return -1.0
        if src == dst:
            return 1.0

        def neighbors(state):
            node, acc = state
            for nxt, weight in graph[node].items():
                yield (nxt, acc * weight)

        for node, acc in multi_source_bfs([(src, 1.0)], neighbors, key=lambda s: s[0]):
            if node == dst:
                return acc
        return -1.0

    return [answer(a, b) for a, b in queries]
