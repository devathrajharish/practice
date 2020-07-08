# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
#
# Find out how many ways to assign symbols to make sum of integers equal to target S.
#
# Example 1:
#
# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# There are 5 ways to assign symbols to make the sum of nums be target 3.
from collections import defaultdict
def main():

    def findTargetsumWays(nums, s):
        if len(nums) == 0:
            return 0

        prev = defaultdict(int)
        prev[nums[0]] += 1
        prev[-nums[1]] += 1

        for i in range(1, len(nums)):
            temp = defaultdict(int)
            for k,v in prev.items():
                temp[k-nums[i]] += v
                temp[k+nums[i]] += v
            prev = temp

        return prev[s]




    nums = [1,1,1,1,1]
    s = 3
    print(findTargetsumWays(nums, s))

if __name__ == '__main__':
    main()