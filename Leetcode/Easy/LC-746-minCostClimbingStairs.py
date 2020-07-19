def main():

    def minCostClimbingStairs(cost):

        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1

        return min(f1,f2)


    cost = [1,4,1,2,3,1]
    print(minCostClimbingStairs(cost))

if __name__ == '__main__':
    main()