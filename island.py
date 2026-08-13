def numIslands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    island_count = 0

    def dfs(r, c):
        if (r < 0 or r >= rows or
            c < 0 or c >= cols or
            grid[r][c] == '0' or
            (r, c) in visited):
            return
        visited.add((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                island_count += 1
                dfs(r, c)

    return island_count

grid = []
rows = int(input("Enter the number of rows in the grid: ")) 
cols = int(input("Enter the number of columns in the grid: "))
for i in range(rows):
    row = input(f"Enter row {i + 1} (as a string of '0's and '1's): ")
    grid.append(list(row))

print(f"The number of islands in the given grid is: {numIslands(grid)}")