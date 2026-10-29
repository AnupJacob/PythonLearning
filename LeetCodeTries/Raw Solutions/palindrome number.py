# ---------------------------------

# File          : palindrome number.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 29/10/2026
# Modified Date :
# Description   : Finding palindrome of a number without converting the integer to a string?
# Licensing     : AnupJake
# ----------------------------------

'''
Given an integer x, return true if x is a palindrome, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1


Follow up: Could you solve it without converting the integer to a string?
'''

def isPalindrome(x):
    checkx = x
    numx = 0

    if checkx <= 0:
        return False
    elif checkx == 0:
        return True
    else:
        while x != 0:
            modx = x%10
            numx = numx*10 + modx
            x = x//10
            print(modx)

        print(numx)
        if numx == checkx:
            result = True
        else:
            result = False

    return result


if __name__ == '__main__':

    num = 1221
    print(isPalindrome(num))
