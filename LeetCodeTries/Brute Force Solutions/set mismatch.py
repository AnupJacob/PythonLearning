# ---------------------------------

# File          : set mismatch.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 12/11/2026
# Modified Date :
# Description   : Finding the repetitive number and missing number in the set causing mismatch
# Licensing     : AnupJake
# ----------------------------------

'''
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.



Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]


Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104


'''
class Solution:
    def findErrorNums(nums):
        result = []
        dummy = []
        lennums = len(nums)

        for i in range(0,lennums):
            if nums[i] not in dummy:
                dummy.append(nums[i])
            else:
                result.append(nums[i])

        for i in range(1,lennums+1):
            if i not in nums:
                result.append(i)


        return result

    if __name__ == "__main__":
        nums = [1,1]

        print(findErrorNums(nums))