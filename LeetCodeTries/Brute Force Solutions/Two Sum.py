# ---------------------------------

# File          : Two Sum.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 27/10/2026
# Modified Date : 28/10/2026
# Description   : Finding indices of sum of two numbers resulting in a target
# Licensing     : AnupJake
# ----------------------------------

'''
1. Two Sum

You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9

Output: [0,1]

Explanation:

The sum of nums[0] and nums[1] is 2 + 7 = 9, which equals the target. Therefore, the indices [0, 1] are returned.

Example 2:

Input: nums = [3,2,4], target = 6

Output: [1,2]

Explanation:

The sum of nums[1] and nums[2] is 2 + 4 = 6, which equals the target. Therefore, the indices [1, 2] are returned.

Example 3:

Input: nums = [3,3], target = 6

Output: [0,1]

Explanation:

The sum of nums[0] and nums[1] is 3 + 3 = 6, which equals the target. Therefore, the indices [0, 1] are returned.



Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity? '''

# Raw solution
def twoSum(nums, target):
    result = []
    numindex = []
    numlen = len(nums)
    print("The number of elements in the list provided is :"+str(numlen))

    for i in range(0,numlen):
        for j in range(0,numlen):
            if i <= j and (nums[i] + nums[j] == 9):
                result.append(nums[i])
                numindex.append(i)
                result.append(nums[j])
                numindex.append(j)
    print("The numbers adding to the "+str(target)+" is "+str(result))
    print("The indices adding to the "+str(target)+" is "+str(numindex))



if __name__ == "__main__":
    target = 9
    numslist = [2,7,11,15]
    twoSum(numslist,target)