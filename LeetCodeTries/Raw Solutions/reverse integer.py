# ---------------------------------

# File          : reverse integer.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 28/10/2026
# Modified Date :
# Description   : Finding reverse of an integer without using any functions (including negetive values)
# Licensing     : AnupJake
# ----------------------------------

'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1
'''

def reverse(x):
    result = ""
    absnum = abs(x)
    strnum = str(absnum)
    lennum = len(strnum)
    print(strnum)

    if absnum > 0:
        for i in range (lennum-1,-1,-1):
            result = result + strnum[i]
    else:
        result = str(0)

    if x < 0:
        result = str(int(result) * -1)

    return(int(result))



if __name__ == "__main__":
    num = -123
    print(reverse(num))