"""Reshaper for questions/q044_word_search.

Converts this question's (board, word) -> bool I/O into the state shape the
shared generate_all() engine understands: a partial state is a (row, col,
matched_index, visited_cells) tuple, expanded to a neighbor whose letter
matches the next character of `word`; a state is complete once it has
matched the whole word. The board contains a match iff generate_all() finds
at least one complete state from some starting cell.
"""
from .. import algorithm as _algorithm
generate_all = _algorithm.generate_all


def solve(board, word):
    if not word:
        return True
    if not board or not board[0]:
        return False

    rows, cols = len(board), len(board[0])
    n = len(word)

    def expand(state):
        r, c, idx, visited = state
        options = []
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and (nr, nc) not in visited
                and board[nr][nc] == word[idx + 1]
            ):
                new_state = (nr, nc, idx + 1, visited | {(nr, nc)})
                options.append((new_state, idx + 1 == n - 1))
        return options

    for r in range(rows):
        for c in range(cols):
            if board[r][c] != word[0]:
                continue
            if n == 1:
                return True
            initial = (r, c, 0, frozenset({(r, c)}))
            if generate_all(initial, expand):
                return True
    return False
