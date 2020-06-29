def main():

    def findLength(A, B):
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1
        return max(max(row) for row in memo)

    A = [1,2,3,2,1]
    B = [3,2,1,4,7]
    print(findLength(A,B))

if __name__ == '__main__':
    main()
