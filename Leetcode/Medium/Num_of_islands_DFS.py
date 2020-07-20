def dfs(grid, r, c):
    new_row = len(grid)
    new_col = len(grid[0])

    grid[r][c] = '0'
    if r - 1 >= 0 and grid[r-1][c] == '1':
        dfs(grid, r - 1, c)
    if r + 1 < new_row and grid[r+1][c] == '1':
        dfs(grid, r + 1, c)
    if c - 1 >= 0 and grid[r][c-1] == '1':
        dfs(grid, r, c - 1)
    if c + 1 < new_col and grid[r][c+1] == '1':
        dfs(grid, r, c + 1)

def num_of_islands(grid):

    num_island = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                num_island += 1
                dfs(grid,i,j)

    return num_island



# grid = [['1','1','1','1','0'],
#         ['1','1','0','1','0'],
#         ['1','1','0','0','0'],
#         ['0','0','0','0','0']]

grid = [['1','1','0','0','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','0'],
        ['0','0','0','1','1']]
print(num_of_islands(grid))