def main():

    def minPathSum(grid):
        n = len(grid)
        m = len(grid[0])

        for i in range(1,m):
            grid[0][i] =grid[0][i] + grid[0][i-1]

        for j in range(1, n):
            grid[j][0] = grid[j-1][0] + grid[j][0]

        for i in range(1,n):
            for j in range(1,m):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]

        print(grid)
        return grid[-1][-1]



    grid = [[1,3,1],
            [1,5,1],
            [4,2,1]]

    print(minPathSum(grid))
if __name__ == '__main__':
    main()