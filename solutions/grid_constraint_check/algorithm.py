def all_groups_unique(entries):
    """Generic constraint check: a value must appear at most once within any
    group it belongs to. `entries` is an iterable of (value, group_ids)
    pairs, where group_ids is a tuple of hashable identifiers naming every
    partition the entry participates in (e.g. its row, its column, and its
    3x3 box on a Sudoku board). Returns True iff no two entries that share a
    group id also share a value in that group. O(n) time/space for n
    entries.

    This is a single-pass constraint check, not a search over an implicit
    graph, so it does not build on the shared _meta.explore() engine -- there
    is no frontier to traverse, just membership bookkeeping.
    """
    seen = set()
    for value, group_ids in entries:
        for group_id in group_ids:
            key = (group_id, value)
            if key in seen:
                return False
            seen.add(key)
    return True
