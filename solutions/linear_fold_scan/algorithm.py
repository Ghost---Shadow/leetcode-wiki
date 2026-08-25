from .._meta.algorithm import explore


def linear_fold(items, init, step):
    """A single left-to-right pass over `items`, carrying an accumulator
    forward via `step(acc, item) -> new_acc`, starting from `init`.
    Returns the final accumulator.

    This is the plain, general left-fold: Roman numeral decoding folds
    over (value, next_value) lookahead pairs; Roman numeral encoding
    folds over a fixed value/symbol table, greedily consuming as much of
    the remaining amount as each entry allows; First Unique Character
    folds a frequency count and then folds again to find the first index
    whose count is 1; Longest Common Prefix folds over the columns of the
    first string, extending the prefix while every other string still
    agrees; Reverse Words in a String folds the word list with a
    prepend-to-accumulator (a left fold with cons reverses the sequence);
    and Palindrome Number folds the decimal digits into their reversal.
    Each is the same "carry an accumulator across one pass" shape with a
    different `step`.

    Instantiation of the shared _meta explore() engine: the degenerate
    single-successor chain over indices 0..len(items)-1 (a plain left
    fold, generalizing kadane_running_extremes's running-best pattern to
    an arbitrary, non-comparison-based accumulator).
    """
    items = list(items)
    n = len(items)

    def transition(i):
        return (i + 1,) if i + 1 < n else ()

    acc = init
    for i in explore((0,) if n else (), transition):
        acc = step(acc, items[i])
    return acc
