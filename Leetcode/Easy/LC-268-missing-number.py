def main():
    nums = [0,2,4,1]
    def missing(nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number


    print(missing(nums))
if __name__ == '__main__':
    main()
