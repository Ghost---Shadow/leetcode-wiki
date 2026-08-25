def solve(s):
    """Optimal: a single linear pass that splits on whitespace (collapsing
    runs and trimming ends), then reverses the word list. O(n) time."""
    words = s.split()
    words.reverse()
    return " ".join(words)
