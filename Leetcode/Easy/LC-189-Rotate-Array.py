def main():

    nums = [1,2,3,4,5,6,7]
    k = 3
    def rotate_array(nums, k):
        nums[:] = nums[(len(nums)-k):] + nums[:(len(nums)-k)]
        return nums
    print(rotate_array(nums, k))


if __name__ == '__main__':
    main()