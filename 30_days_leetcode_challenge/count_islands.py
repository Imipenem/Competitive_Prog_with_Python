def numIslands(grid: [[]]) -> int:
    islands = 0
    if not grid: return 0
    width = len(grid[0])
    height = len(grid)

    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if grid[j][i] == "1":
                mark_island(j, i, height, width, grid)
                islands += 1
    return islands


def mark_island(i, j, width, height, grid):
    if i == -1 or i >= width or j == -1 or j >= height or grid[i][j] == "0" or grid[i][j] == 'X': return
    grid[i][j] = 'X'
    mark_island(i - 1, j, width, height, grid)
    mark_island(i + 1, j, width, height, grid)
    mark_island(i, j - 1, width, height, grid)
    mark_island(i, j + 1, width, height, grid)


if __name__ == "__main__":
    print(numIslands(["1"]))