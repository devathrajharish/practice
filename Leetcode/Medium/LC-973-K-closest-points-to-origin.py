import math
import heapq
def main():
    points = [[1,3],[-2,2]]
    k = 1
    arr = [(math.sqrt(x**2 + y**2), x, y) for x,y in points]
    heapq.heapify(arr)
    result = []

    while(len(result)) < k:
        dist, x, y = heapq.heappop(arr)
        result.append([x,y])

    print(result)




if __name__ == '__main__':
    main()