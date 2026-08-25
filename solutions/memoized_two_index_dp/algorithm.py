from .._meta.algorithm import explore


def grid_dp(cells, compute):
    """Computes a 2-D memoized DP table over a caller-supplied, already
    topologically-sorted sequence of (i, j) coordinates by walking that
    sequence as a trivial chain 0 -> 1 -> ... -> len(cells) - 1 with the
    shared explore() engine.

    Knobs:
      state shape  -- a single integer index into `cells` (which itself
                      holds the real (i, j) grid coordinates).
      discipline   -- "fifo", though it doesn't matter: each state has
                      exactly one successor, so the walk never branches.
      transition   -- stateful; on visiting position k it looks up
                      (i, j) = cells[k], calls compute(i, j, table) to
                      fill table[(i, j)], then advances to k + 1. The
                      caller is responsible for ordering `cells` so every
                      cell's dependencies were already visited (e.g.
                      row-major order for edit distance / maximal square /
                      regex matching, where (i, j) only depends on
                      (i-1, j), (i, j-1), (i-1, j-1) or (i, j-2); or
                      increasing-substring-length order for palindrome
                      DPs, where (l, r) depends on (l+1, r-1)).
      fold         -- none needed inside explore; the caller reads
                      whatever entries of the finished `table` it needs
                      once the walk completes.

    compute(i, j, table) -> value for cell (i, j); may read table[(i', j')]
    for any already-visited cell via closure to implement whichever 2-D
    recurrence the question needs (edit-distance minimization, square-side
    DP, regex/wildcard matching, palindrome-range membership, etc.).

    Returns the completed `table` dict, keyed by (i, j).
    """
    cell_list = list(cells)
    table = {}

    def transition(k):
        i, j = cell_list[k]
        table[(i, j)] = compute(i, j, table)
        if k + 1 < len(cell_list):
            return [k + 1]
        return []

    if cell_list:
        list(explore([0], transition, order="fifo"))
    return table
