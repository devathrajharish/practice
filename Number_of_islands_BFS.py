def no_of_islands(grid):

    row = len(grid)
    col = len(grid[0])
    bfs = []
    no_of_island = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1':

                no_of_island += 1
                bfs.append((i,j))

                while bfs:
                    popped = bfs.pop()
                    row_new, col_new = popped[0], popped[1]
                    grid[row_new][col_new] = "v"

                    if row_new -1 >= 0 and grid[row_new-1][col_new] == '1':
                        bfs.append((row_new-1, col_new))

                    if col_new >=0 and grid[row_new][col_new] == '1':
                        bfs.append((row_new, col_new-1))

                    if row_new+1 < len(grid) and grid[row_new+1][col_new] == '1':
                        bfs.append((row_new+1, col_new))

                    if col_new+1 < len(grid[0]) and grid[row_new][col_new+1] == '1':
                        bfs.append((row_new,col_new+1))

    return no_of_island



grid = [['1','1','0','0','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','0'],
        ['0','0','0','1','1']]
print(no_of_islands(grid))