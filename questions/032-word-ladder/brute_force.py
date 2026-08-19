def solve(begin_word, end_word, word_list):
    """Brute-force BFS: at every step, check every word in the word list
    against the current word by comparing full strings character by character
    (no precomputed adjacency / wildcard buckets), instead of building a
    pattern-based graph up front. O(n^2 * L) per level."""
    from collections import deque

    words = set(word_list)
    if end_word not in words:
        return 0

    def one_diff(a, b):
        diff = 0
        for ca, cb in zip(a, b):
            if ca != cb:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1

    visited = {begin_word}
    queue = deque([(begin_word, 1)])
    while queue:
        word, steps = queue.popleft()
        if word == end_word:
            return steps
        for candidate in list(words):
            if candidate not in visited and one_diff(word, candidate):
                visited.add(candidate)
                queue.append((candidate, steps + 1))
    return 0
