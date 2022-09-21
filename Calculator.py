# ---------------------------------

# File          : Calculator.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 27/04/2022
# Modified Date : 
# Description   : Sample program to create a calculator functionality
# Licensing     : Anup Jacob, LYIT
# ----------------------------------


if __name__ == '__main__':

    #num1 = 20
    #num2 = 10
    #oper = '/'
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    oper = input("Enter the operation to be performed :")
    print(type(num1),type(num2),type(oper))
    if oper == "+":
        result = num1 + num2
        print("\nThe result of the sum is", result)
    elif oper == "-":
        result = num1 - num2
        print("\nThe result of the subtraction is", result)
    elif oper == "*":
        result = num1 * num2
        print("\nThe result of multiplication is", result)
    elif oper == "/":
        result = num1 / num2
        print("\nThe result of division is", result)
    else:
        print("\nWrong choice of operation")

    print("\nThank you for using my calculator application")




