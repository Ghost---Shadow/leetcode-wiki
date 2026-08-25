def solve(board, word):
    """Brute-force DFS/backtracking with no pruning heuristics, walked with an
    explicit stack of (row, col, matched-so-far, next-direction) frames
    instead of recursion -- same worst-case exponential search."""
    if not board or not board[0] or not word:
        return not word

    rows, cols = len(board), len(board[0])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def backtrack(sr, sc):
        if board[sr][sc] != word[0]:
            return False
        board[sr][sc] = "#"
        stack = [[sr, sc, 0, 0]]
        while stack:
            r, c, idx, d = stack[-1]
            if idx + 1 == len(word):
                return True
            advanced = False
            while d < 4:
                dr, dc = dirs[d]
                d += 1
                stack[-1][3] = d
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == word[idx + 1]:
                    board[nr][nc] = "#"
                    stack.append([nr, nc, idx + 1, 0])
                    advanced = True
                    break
            if not advanced:
                board[r][c] = word[idx]
                stack.pop()
        return False

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c):
                return True
    return False
