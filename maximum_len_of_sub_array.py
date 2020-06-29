def main():

    def findLength(A,B):
        m = [[0 for i in range(len(A) + 1)] for j in range(len(B) + 1)]
        maxi = 0
        for i in range(1, len(m)):
            for j in range(1, len(m[0])):
                if A[i - 1] == B[j - 1]:
                    m[i][j] = 1 + m[i - 1][j - 1]
                    maxi = max(maxi, m[i][j])
        return maxi

    A = [1,2,3,2,1]
    B = [3,2,1,4,7]
    print(findLength(A,B))

if __name__ == '__main__':
    main()
