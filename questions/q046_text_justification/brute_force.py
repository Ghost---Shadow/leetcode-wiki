def solve(words, maxWidth):
    """Brute-force: greedily packs as many words per line as fit, then for full
    lines distributes the extra spaces one unit at a time in a round-robin sweep
    over the gaps until they're used up, instead of computing the exact per-gap
    space counts directly via divmod."""
    lines = []
    i = 0
    n = len(words)
    while i < n:
        j = i
        line_len = 0
        cur_words = []
        while j < n and line_len + len(words[j]) + len(cur_words) <= maxWidth:
            cur_words.append(words[j])
            line_len += len(words[j])
            j += 1

        is_last_line = j == n
        if is_last_line or len(cur_words) == 1:
            line = " ".join(cur_words)
            line += " " * (maxWidth - len(line))
            lines.append(line)
        else:
            total_spaces = maxWidth - line_len
            gaps = len(cur_words) - 1
            slots = [0] * gaps
            idx = 0
            for _ in range(total_spaces):
                slots[idx % gaps] += 1
                idx += 1
            line = cur_words[0]
            for k in range(1, len(cur_words)):
                line += " " * slots[k - 1] + cur_words[k]
            lines.append(line)

        i = j
    return lines
