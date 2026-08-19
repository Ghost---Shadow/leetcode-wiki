def solve(words, maxWidth):
    """Optimal: single greedy pass to pack words per line (this is the standard
    optimal approach for this problem), computing each gap's exact space count
    directly via divmod instead of a round-robin sweep -- O(n) time overall
    (each word processed once), O(1) extra bookkeeping per line."""
    lines = []
    i = 0
    n = len(words)
    while i < n:
        j = i
        line_len = 0
        while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
            line_len += len(words[j])
            j += 1

        cur_words = words[i:j]
        is_last_line = j == n
        gaps = len(cur_words) - 1

        if is_last_line or gaps == 0:
            line = " ".join(cur_words)
            line += " " * (maxWidth - len(line))
            lines.append(line)
        else:
            total_spaces = maxWidth - line_len
            space, extra = divmod(total_spaces, gaps)
            parts = [cur_words[0]]
            for k in range(1, len(cur_words)):
                gap_size = space + (1 if k <= extra else 0)
                parts.append(" " * gap_size)
                parts.append(cur_words[k])
            lines.append("".join(parts))

        i = j
    return lines
