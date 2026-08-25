def solve(grid):
    """Brute-force flood fill: DFS from every unvisited land cell, marking
    the whole island as visited before moving on."""
    if not grid or not grid[0]:
        return 0
    grid = [row[:] for row in grid]
    rows, cols = len(grid), len(grid[0])
    count = 0

    def flood_fill(r, c):
        stack = [(r, c)]
        while stack:
            cr, cc = stack.pop()
            if cr < 0 or cr >= rows or cc < 0 or cc >= cols:
                continue
            if grid[cr][cc] != "1":
                continue
            grid[cr][cc] = "0"
            stack.extend([(cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                flood_fill(r, c)
    return count
