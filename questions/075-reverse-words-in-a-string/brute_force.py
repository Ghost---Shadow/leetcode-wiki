def solve(s):
    """Brute-force: repeatedly rfind the last whitespace-delimited word from
    the end of the (shrinking) remaining string and append it, an O(n^2)
    approach that rescans the string on every word instead of a single
    linear split-and-reverse pass."""
    remaining = s
    words = []
    n = len(remaining)
    end = n
    i = n - 1
    while i >= 0:
        if remaining[i] == " ":
            if i + 1 < end:
                words.append(remaining[i + 1:end])
            end = i
            i -= 1
        else:
            i -= 1
    if end > 0:
        words.append(remaining[0:end])
    return " ".join(words)
