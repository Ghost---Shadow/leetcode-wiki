"""The one engine behind every technique directory in solutions/.

Every technique here is a configuration of the same meta-algorithm:

    answer = fold(explore(seeds, transition, order))

`explore` lazily *unfolds* an implicit state graph (pop a state from the
frontier, yield it, push its successors); the caller *folds* the stream of
yielded states into an answer. In recursion-scheme terms explore is the
anamorphism and the fold is the catamorphism; a technique is just a choice
of four knobs:

  1. state shape        -- index, partial solution, (slow, fast) pair,
                           graph node, interval, window, ...
  2. frontier discipline -- LIFO = depth-first, FIFO = breadth-first,
                           priority = best-first; a single-successor
                           transition degenerates to a plain fold/iteration
  3. transition          -- the branching rules; owns pruning, dedup and
                           memoization (explore keeps no visited set on
                           purpose -- that knob is what separates a brute
                           force from a DP on the same state graph)
  4. fold                -- collect / max / first-hit / append-in-order

See solutions/README.md for the taxonomy of current instantiations.
"""
from collections import deque
import heapq


def explore(initial_states, transition, order="lifo", priority=None):
    """Lazily enumerates the states of an implicit graph.

    initial_states -- iterable of seed states for the frontier.
    transition(state) -- iterable of successor states. May be stateful
        (e.g. Kahn's decrements shared in-degree counts as it releases
        neighbors) and is in charge of cycle avoidance / deduplication /
        memoization: explore itself keeps no visited set.
    order -- "lifo" (depth-first), "fifo" (breadth-first) or "priority"
        (best-first; requires `priority`).
    priority(state) -- sortable key, consulted when order="priority".
        States themselves never need to be comparable; ties break by
        insertion sequence.

    Yields each state at the moment it leaves the frontier. With a
    single-successor transition this is a plain iteration -- the
    degenerate chain that turns the engine into a left fold.
    """
    if order == "lifo":
        frontier = list(initial_states)
        while frontier:
            state = frontier.pop()
            yield state
            frontier.extend(transition(state))
    elif order == "fifo":
        frontier = deque(initial_states)
        while frontier:
            state = frontier.popleft()
            yield state
            frontier.extend(transition(state))
    elif order == "priority":
        if priority is None:
            raise ValueError('order="priority" requires a priority function')
        seq = 0
        frontier = []
        for state in initial_states:
            heapq.heappush(frontier, (priority(state), seq, state))
            seq += 1
        while frontier:
            _, _, state = heapq.heappop(frontier)
            yield state
            for nxt in transition(state):
                seq += 1
                heapq.heappush(frontier, (priority(nxt), seq, nxt))
    else:
        raise ValueError(f"Unknown order: {order!r}")
