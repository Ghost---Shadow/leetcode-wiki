from .._meta.algorithm import explore


def chain_dp(n, compute):
    """Computes a 1-D memoized DP table over indices 0..n (inclusive) by
    walking the trivial index chain 0 -> 1 -> ... -> n with the shared
    explore() engine.

    Knobs:
      state shape  -- a single integer index i.
      discipline   -- "fifo", but it doesn't matter here since each state
                      has exactly one successor: the chain never branches.
      transition   -- stateful; on visiting i it calls compute(i, table)
                      to fill table[i], then advances to i + 1. All the
                      question-specific recurrence logic (which earlier
                      indices to look back at, how to combine them) lives
                      in `compute`, not in the walk itself.
      fold         -- none needed inside explore; the caller reads
                      whatever entries of the finished `table` it needs
                      once the walk completes.

    compute(i, table) -> value for index i; may read table[j] for any
    j < i (already memoized) via closure to implement whichever 1-D
    recurrence the question needs: a Fibonacci-style count (climbing
    stairs), a max-of-two-choices (house robber), a min-over-choices
    (coin change amounts), a max-over-predecessors (longest increasing
    subsequence), a boolean OR over predecessors (word break, jump
    game reachability), a min-over-predecessors (jump game II hops), or
    a lookback recurrence (longest valid parentheses).

    Returns the completed `table` dict, keyed 0..n.
    """
    table = {}

    def transition(i):
        table[i] = compute(i, table)
        if i < n:
            return [i + 1]
        return []

    list(explore([0], transition, order="fifo"))
    return table
