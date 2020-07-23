def main():

    def Trapwater(area):
        left_max = 0
        right_max = 0
        i = 0
        j = len(area) -1
        res = 0
        while i < j:
            left_max = max(left_max, area[i])
            right_max = max(right_max, area[j])

            if area[i] < area[j]:
                if area[i] < left_max:
                    res = res + left_max - area[i]
                else:
                    res += 0
                i = i+ 1

            else:
                if area[j] < right_max:
                    res += right_max- area[j]
                else:
                    res += 0
                j = j-1
        return res
    area = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(Trapwater(area))

if __name__ == '__main__':
    main()