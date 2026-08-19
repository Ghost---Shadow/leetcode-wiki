from collections import Counter


def solve(board, word):
    """Optimal: DFS backtracking with in-place visited marking (the standard
    approach for this problem -- there's no asymptotically better algorithm), made
    efficient by: (1) an upfront letter-frequency check to bail out immediately if
    the board can't possibly contain word's letters, (2) reversing word when its
    last-letter count is rarer than its first-letter count so the search fails
    faster, and (3) bounds/character checks done before recursing instead of at
    the top of the call, avoiding a function call per out-of-bounds step."""
    if not word:
        return True
    if not board or not board[0]:
        return False

    rows, cols = len(board), len(board[0])

    board_counts = Counter(ch for row in board for ch in row)
    word_counts = Counter(word)
    for ch, cnt in word_counts.items():
        if board_counts[ch] < cnt:
            return False

    # Search from the rarer end first to prune faster.
    if board_counts[word[0]] > board_counts[word[-1]]:
        word = word[::-1]

    n = len(word)

    def backtrack(r, c, idx):
        board[r][c] = "#"
        if idx + 1 == n:
            board[r][c] = word[idx]
            return True

        found = False
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == word[idx + 1]:
                if backtrack(nr, nc, idx + 1):
                    found = True
                    break
        board[r][c] = word[idx]
        return found

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0] and backtrack(r, c, 0):
                return True
    return False
