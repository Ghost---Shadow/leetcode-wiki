from .._meta.algorithm import explore


def hashmap_pass(items, step, table=None):
    """Single left-to-right pass over `items`, carrying one hashmap
    `table` forward and calling `step(table, index, item)` at each
    position.

    `step` may mutate `table` in place and/or return a non-None value to
    short-circuit the pass -- Two Sum's step returns the matching
    [prior_index, index] pair the instant a complement is already in the
    table. If `step` never returns non-None the pass runs to completion
    and the final `table` holds whatever was accumulated along the way --
    Group Anagrams' step buckets by a per-string signature (never
    short-circuits, wants the whole table); Valid Anagram's step consumes
    a running frequency count built from the other string (short-circuits
    on the first sign of mismatch).

    Returns (early_result, table): `early_result` is the first non-None
    value `step` produced, or None if the pass ran to completion.

    Instantiation of the shared _meta explore() engine: the degenerate
    single-successor chain over indices 0..len(items)-1 (a plain left
    fold), carrying `table` in the fold's accumulator and simply not
    requesting explore's next state once `step` fires.
    """
    if table is None:
        table = {}

    def transition(i):
        return (i + 1,) if i + 1 < len(items) else ()

    for i in explore((0,) if items else (), transition):
        result = step(table, i, items[i])
        if result is not None:
            return result, table
    return None, table
