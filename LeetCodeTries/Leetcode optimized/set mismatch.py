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


brute force test
def findErrorNums(nums):
    dummy = []
    result = []
    lennums = len(nums)
    setnums = set(nums)

    for i in range(0, lennums):
        if nums[i] in dummy:
            result.append(nums[i])
        dummy.append(nums[i])

    for i in range(1,lennums+1):
        if i not in setnums:
            result.append(i)

    return result
'''
def findErrorNums(nums):
    lennums = len(nums)
    sumnums =sum(nums)
    setnums = set(nums)
    sumsetnums = sum(setnums)
    actualsum = lennums * (lennums + 1) // 2

    return (sumnums-sumsetnums, actualsum-sumsetnums)

if __name__ == "__main__":
    nums = [1, 2, 2, 4]
    print("The result is :",findErrorNums(nums))