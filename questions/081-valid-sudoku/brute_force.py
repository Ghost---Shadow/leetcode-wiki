def solve(board):
    """Brute-force: for every filled cell, independently rescan its entire
    row, column, and 3x3 box from scratch to check for duplicates. Does
    O(81 * 27) redundant work instead of a single pass with hash sets."""
    rows = len(board)
    cols = len(board[0]) if rows else 0

    for r in range(rows):
        for c in range(cols):
            val = board[r][c]
            if val == ".":
                continue

            # check row
            if sum(1 for cc in range(cols) if board[r][cc] == val) > 1:
                return False

            # check column
            if sum(1 for rr in range(rows) if board[rr][c] == val) > 1:
                return False

            # check 3x3 box
            box_r, box_c = (r // 3) * 3, (c // 3) * 3
            count = 0
            for rr in range(box_r, box_r + 3):
                for cc in range(box_c, box_c + 3):
                    if board[rr][cc] == val:
                        count += 1
            if count > 1:
                return False

    return True
