def isTriplet(ar, n):

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Calculate square of array elements
                x = ar[i] * ar[i]
                y = ar[j] * ar[j]
                z = ar[k] * ar[k]
                if (x == y + z or y == x + z or z == x + y):
                    return 1

    # If we reach here, no triplet found
    return 0


def main():
    # Driver program to test above function
    ar = [2, 1, 4, 6, 5]
    ar_size = len(ar)

    if (isTriplet(ar, ar_size)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()