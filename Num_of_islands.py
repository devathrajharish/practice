def no_of_islands(grid):
    if grid==[]:
        return 0

    bfs_stack = []
    islands = 0

    for rows in range(len(grid)):
        for col in range(len(grid[0])):
            if(grid[rows][col] == '1'):
                islands += 1
                bfs_stack.append((rows, col))

                while bfs_stack:
                    popped = bfs_stack.pop()
                    popped_i, popped_j = popped[0],popped[1]
                    grid[popped_i][popped_j] = 'v'

                    if(popped_i - 1 >=0  and grid[popped_i -1 ][popped_j] == '1'):
                        bfs_stack.append((popped_i-1, popped_j))

                    if(popped_j - 1 >= 0 and grid[popped_i][popped_j -1 ] == '1'):
                        bfs_stack.append((popped_i, popped_j - 1 ))

                    if( popped_i + 1 < len(grid) and grid[popped_i + 1][popped_j] == '1'):
                        bfs_stack.append((popped_i + 1, popped_j))

                    if(popped_j + 1 < len(grid) and grid[popped_i][popped_j + 1]== '1'):
                        bfs_stack.append((popped_i, popped_j + 1))

    return islands

grid = [['1','1','0','0','0'],['1','1','0','0','0'], ['0','0','1','0','0'],['0','0','0','1','1']]
print(no_of_islands(grid))


