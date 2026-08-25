def solve(chars):
    """Brute-force: build the run-length-encoded string with ordinary string
    concatenation (recomputing run boundaries with a nested scan for each
    position) instead of the in-place two-pointer compression. O(n^2)."""
    n = len(chars)
    result = []
    i = 0
    while i < n:
        j = i
        while j < n and chars[j] == chars[i]:
            j += 1
        run_length = j - i
        result.append(chars[i])
        if run_length > 1:
            result.extend(list(str(run_length)))
        i = j

    chars[:] = result
    return len(chars)
