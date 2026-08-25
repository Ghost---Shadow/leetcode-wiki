from .._meta.algorithm import explore


def multi_source_bfs(seeds, neighbors, key=lambda state: state):
    """FIFO layered exploration seeded from one or more starting states at
    once. `neighbors(state)` yields the states reachable in one step from
    `state`; `key(state)` extracts the hashable identity used to dedup a
    state so it is only ever entered once, independent of any extra payload
    (a step count, an accumulated product, ...) carried alongside it.

    Yields every state (seeds included) in the order it is first visited --
    i.e. in BFS layer order from the seeds. O(V + E) time/space over the
    reachable region.

    Instantiation of the shared _meta explore() engine: FIFO discipline; the
    (stateful) transition owns the visited set and only releases states
    whose key hasn't been seen; the fold is left to the caller since
    different questions want different projections of the visited order
    (shortest step count, max layer reached, the value at a target key...).
    """
    visited = {key(seed) for seed in seeds}

    def transition(state):
        for nxt in neighbors(state):
            k = key(nxt)
            if k not in visited:
                visited.add(k)
                yield nxt

    yield from explore(seeds, transition, order="fifo")


def count_components(nodes, neighbors):
    """Counts connected components over an implicit graph: for every node
    not yet visited, spends one multi_source_bfs() run flooding its whole
    component before moving to the next unvisited node, sharing a single
    visited set across every run. O(V + E) time, O(V) space.
    """
    visited = set()
    count = 0
    for node in nodes:
        if node in visited:
            continue
        count += 1
        visited.add(node)

        def transition(state, _visited=visited):
            for nxt in neighbors(state):
                if nxt not in _visited:
                    _visited.add(nxt)
                    yield nxt

        for _ in explore([node], transition, order="fifo"):
            pass
    return count
