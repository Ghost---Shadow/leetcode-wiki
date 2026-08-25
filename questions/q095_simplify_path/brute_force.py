def solve(path):
    """Brute-force: repeatedly rescans the segment list from the start, removing
    one '.' segment or one '..'-plus-preceding-segment pair per pass, O(n) work
    per removal (O(n^2) overall), instead of a single O(n) stack pass."""
    segments = [seg for seg in path.split('/') if seg != '']

    changed = True
    while changed:
        changed = False
        for i, seg in enumerate(segments):
            if seg == '.':
                del segments[i]
                changed = True
                break
            if seg == '..':
                if i > 0:
                    del segments[i]
                    del segments[i - 1]
                else:
                    del segments[i]
                changed = True
                break

    return '/' + '/'.join(segments)
