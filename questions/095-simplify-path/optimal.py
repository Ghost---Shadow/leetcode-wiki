def solve(path):
    """Optimal: single-pass stack. Each segment is pushed, popped (for '..'), or
    skipped (for '.' / empty) in O(1) amortized, one pass over the split
    segments, O(n) time total instead of repeated O(n) rescans."""
    stack = []
    for seg in path.split('/'):
        if seg == '' or seg == '.':
            continue
        if seg == '..':
            if stack:
                stack.pop()
        else:
            stack.append(seg)

    return '/' + '/'.join(stack)
