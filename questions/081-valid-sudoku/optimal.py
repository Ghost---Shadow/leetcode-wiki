def solve(board):
    """Optimal: single pass over the board, tracking seen digits per row,
    column, and 3x3 box using hash sets (bitmasks would also work since the
    board is fixed 9x9). O(rows*cols) = O(81) = O(1) time for a fixed-size
    board, versus the brute force's redundant O(81*27) rescans."""
    rows = len(board)
    cols = len(board[0]) if rows else 0

    row_seen = [set() for _ in range(rows)]
    col_seen = [set() for _ in range(cols)]
    box_seen = {}

    for r in range(rows):
        for c in range(cols):
            val = board[r][c]
            if val == ".":
                continue
            box_key = (r // 3, c // 3)
            box_set = box_seen.setdefault(box_key, set())

            if val in row_seen[r] or val in col_seen[c] or val in box_set:
                return False

            row_seen[r].add(val)
            col_seen[c].add(val)
            box_set.add(val)

    return True
