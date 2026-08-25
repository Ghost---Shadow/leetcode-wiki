from collections import defaultdict, deque


def solve(begin_word, end_word, word_list):
    """Optimal: build a wildcard-pattern -> words bucket up front (e.g.
    "h*t" -> ["hot", "hit"]), so each BFS step only needs to generate the
    L wildcard variants of the current word and look them up, instead of
    comparing against every other word. O(n * L^2) time, O(n * L) space."""
    words = set(word_list)
    if end_word not in words:
        return 0

    L = len(begin_word)
    buckets = defaultdict(list)
    for word in words:
        for i in range(L):
            pattern = word[:i] + "*" + word[i + 1:]
            buckets[pattern].append(word)

    visited = {begin_word}
    queue = deque([(begin_word, 1)])

    while queue:
        word, steps = queue.popleft()
        if word == end_word:
            return steps
        for i in range(L):
            pattern = word[:i] + "*" + word[i + 1:]
            for candidate in buckets.get(pattern, ()):
                if candidate not in visited:
                    visited.add(candidate)
                    queue.append((candidate, steps + 1))

    return 0
