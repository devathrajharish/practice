import math
import collections
import heapq
def main():

    n = 9
    de = math.ceil(n/2)

    model = [6,6,6,6,7,7,7,7,5]
    C = collections.Counter(model)
    sum = 0
    if n > len(model):
        return 0
    models = 1
    arr = []
    for i in C.values():
        arr.append(i)
    maxheap = heapq.heapify(arr)
    print(maxheap)
    for i in sorted(C.values(), reverse=True):
        sum = sum + i
        if sum >= de:
            models = models + 1
            break
    return models


if __name__ == '__main__':
    main()