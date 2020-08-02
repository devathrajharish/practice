from collections import Counter
def main():
    arr1 = [1, 2, 3, 2]
    arr2 = [4, 3 , 2, 2, 2]


    def intersect(nums1, nums2):
        n1_counter, n2_counter = Counter(nums1), Counter(nums2)
        res = []

        for n1_digit in n1_counter:
            if n1_digit in n2_counter:
                intersecting_times = min(n1_counter[n1_digit], n2_counter[n1_digit])
                res += [n1_digit] * intersecting_times

        return res
    print(intersect(arr1,arr2))
if __name__ == '__main__':
    main()