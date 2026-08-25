def solve(board, word):
    """Brute-force DFS/backtracking: tries every starting cell and all four
    directions at each step with no pruning heuristics (e.g. no trie, no letter
    frequency check) -- worst-case exponential in the word length."""
    if not board or not board[0] or not word:
        return not word

    rows, cols = len(board), len(board[0])

    def backtrack(r, c, idx):
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[idx]:
            return False
        temp = board[r][c]
        board[r][c] = "#"
        found = (
            backtrack(r + 1, c, idx + 1)
            or backtrack(r - 1, c, idx + 1)
            or backtrack(r, c + 1, idx + 1)
            or backtrack(r, c - 1, idx + 1)
        )
        board[r][c] = temp
        return found

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False
