def next_dominant_index(values, dominates):
    """For every index i, finds the nearest index j > i such that
    dominates(values[j], values[i]) is True, using a single-pass monotonic
    stack. Returns a list `nxt` where nxt[i] is that index, or len(values)
    if no such index exists.

    This one routine powers both "next greater element" problems
    (dominates = lambda a, b: a > b) and "next smaller element" problems
    (dominates = lambda a, b: a < b) -- the whole family of monotonic-stack
    problems that ask "how far to the next element that beats this one".
    """
    n = len(values)
    nxt = [n] * n
    stack = []  # indices whose "next dominant" hasn't been found yet
    for i in range(n):
        while stack and dominates(values[i], values[stack[-1]]):
            nxt[stack.pop()] = i
        stack.append(i)
    return nxt
