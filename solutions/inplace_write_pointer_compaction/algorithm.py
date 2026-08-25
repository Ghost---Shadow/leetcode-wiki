def scan_compact(n, step):
    """A read/write two-pointer compaction pass. Starting at read=write=0,
    `step(read, write)` processes the run of input starting at `read`
    (consuming as much of it as it needs -- one element, or a whole run
    of equal elements), writes whatever survives into the output starting
    at `write`, and returns the pair (next_read, next_write). The loop
    continues while read < n; the final `write` is the new logical length
    of the compacted output.

    Move Zeroes (each step consumes exactly one element, advancing write
    only for nonzero values) and String Compression (each step consumes
    a whole run of equal characters at once, writing the character plus
    its run-length digits) are both this same read/write compaction
    shape, differing only in how much of the input one step consumes and
    what it writes.

    Known-outlier pattern per solutions/README.md: in-place compaction
    does not reduce naturally onto the _meta explore() traversal shape --
    there is no useful notion of "successor states" independent of the
    mutation itself, since the whole point is mutating the underlying
    sequence as we go. This is the same category as sort-colors-style
    partitioning, so it is a standalone routine rather than an explore()
    instantiation.
    """
    read, write = 0, 0
    while read < n:
        read, write = step(read, write)
    return write
