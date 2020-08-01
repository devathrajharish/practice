def countBattleship(grid):
    if not grid or not grid[0]:
        return 0
    res = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'X':
                if not(row+1 < len(grid) and grid[row+1][col] =="X" or col+1 < len(grid[0]) and grid[row][col+1] == "X" ):
                    res +=1

    return res


grids = [["X",".",".", "X"],[".",".",".","X"],[".",".",".","X"]]
grid = [[".",".",".", "X"],["X","X","X","X"],[".",".",".","X"]]
print(countBattleship(grid))