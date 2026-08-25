from .._meta.algorithm import explore


def justify_lines(words, max_width):
    """Greedy line-packing + padding: pack as many `words` as fit into each
    line of width `max_width` (each line greedily takes the next word as
    long as it still fits with single spaces between words already on the
    line), then distribute the leftover width as padding -- evenly between
    gaps (extra space going to the leftmost gaps first) for a fully packed
    line, or all trailing on the right for the last line or a one-word
    line. O(n) time overall (each word visited once), O(1) extra
    bookkeeping per line.

    This is a genuine outlier among this repo's techniques: unlike the
    shared graph-exploration engine other techniques instantiate, line
    packing has no natural state-graph shape to explore -- it's a two-
    level greedy grouping (pack a line, then pad it) with no meaningful
    branching or backtracking. It's still expressed as one instantiation
    of the shared _meta explore() engine for consistency: the degenerate
    single-successor chain walking the starting index of each successive
    line, folded into the list of finished, padded lines.
    """
    n = len(words)

    def line_end(start):
        j = start
        line_len = 0
        while j < n and line_len + len(words[j]) + (j - start) <= max_width:
            line_len += len(words[j])
            j += 1
        return j

    def transition(start):
        end = line_end(start)
        return (end,) if end < n else ()

    lines = []
    for start in explore((0,) if words else (), transition):
        end = line_end(start)
        cur_words = words[start:end]
        is_last_line = end == n
        gaps = len(cur_words) - 1

        if is_last_line or gaps == 0:
            line = " ".join(cur_words)
            line += " " * (max_width - len(line))
            lines.append(line)
        else:
            line_len = sum(len(w) for w in cur_words)
            total_spaces = max_width - line_len
            space, extra = divmod(total_spaces, gaps)
            parts = [cur_words[0]]
            for k in range(1, len(cur_words)):
                gap_size = space + (1 if k <= extra else 0)
                parts.append(" " * gap_size)
                parts.append(cur_words[k])
            lines.append("".join(parts))

    return lines
