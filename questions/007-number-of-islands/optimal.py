from collections import deque


def solve(grid):
    """Optimal: BFS flood fill from every unvisited land cell. O(rows*cols) time, O(min(rows,cols)) space
    for the queue in the worst case (asymptotically same class as DFS, but avoids Python recursion-depth
    issues and uses an explicit queue rather than a growing stack of unbounded neighbors)."""
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = "0"
        while queue:
            cr, cc = queue.popleft()
            for nr, nc in ((cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    grid[nr][nc] = "0"
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                bfs(r, c)
    return count
