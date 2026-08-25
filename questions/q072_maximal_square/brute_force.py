def solve(matrix):
    """Brute-force: for every cell as a potential top-left corner, try every
    possible square size and re-scan all its cells to check they're all '1'.
    O(rows*cols*min(rows,cols)^3) instead of the O(rows*cols) DP approach."""
    if not matrix or not matrix[0]:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    best = 0

    def is_all_ones(r, c, size):
        for i in range(r, r + size):
            for j in range(c, c + size):
                if matrix[i][j] != "1":
                    return False
        return True

    for r in range(rows):
        for c in range(cols):
            max_size = min(rows - r, cols - c)
            for size in range(1, max_size + 1):
                if is_all_ones(r, c, size):
                    best = max(best, size)
                else:
                    break
    return best * best
