def solve(s):
    """Optimal: Manacher's algorithm. O(n) time, O(n) space.

    Transforms the string by interleaving sentinels (e.g. "aba" -> "^#a#b#a#$")
    so every palindrome (odd or even length) has odd length in the transformed
    string, then computes palindrome radii in a single linear pass using
    previously computed radii to skip redundant comparisons.
    """
    if not s:
        return ""

    t = "^#" + "#".join(s) + "#$"
    n = len(t)
    radius = [0] * n
    center = right = 0

    for i in range(1, n - 1):
        if i < right:
            mirror = 2 * center - i
            radius[i] = min(right - i, radius[mirror])

        while t[i + radius[i] + 1] == t[i - radius[i] - 1]:
            radius[i] += 1

        if i + radius[i] > right:
            center, right = i, i + radius[i]

    max_len = 0
    center_index = 0
    for i in range(1, n - 1):
        if radius[i] > max_len:
            max_len = radius[i]
            center_index = i

    start = (center_index - max_len) // 2
    return s[start:start + max_len]
