import importlib.util
import os

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "meta_algorithm", os.path.join(_here, "..", "_meta", "algorithm.py"))
_meta = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_meta)
explore = _meta.explore


def kahn_topological_order(num_nodes, edges):
    """Kahn's BFS topological sort over a directed graph with `num_nodes`
    nodes (0..num_nodes-1) and `edges` as (u, v) pairs meaning u -> v.

    Returns a list of all nodes in topological order, or None if the graph
    has a cycle (fewer than num_nodes nodes could be ordered). O(V + E).

    Instantiation of the shared _meta explore() engine: FIFO discipline
    seeded with every zero-in-degree node; the (stateful) transition
    releases a neighbor the moment its last unprocessed prerequisite is
    consumed; the fold appends states in the order they leave the frontier.
    """
    adjacency = [[] for _ in range(num_nodes)]
    indegree = [0] * num_nodes
    for u, v in edges:
        adjacency[u].append(v)
        indegree[v] += 1

    def transition(node):
        released = []
        for nxt in adjacency[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                released.append(nxt)
        return released

    seeds = [i for i in range(num_nodes) if indegree[i] == 0]
    order = list(explore(seeds, transition, order="fifo"))
    return order if len(order) == num_nodes else None
