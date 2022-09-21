# ---------------------------------

# File          : Average.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 28/04/2022
# Modified Date : 
# Description   : Average of list of numbers
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

import math

def average():

    value = []
    sumnum = 0

    number = int(input("Enter the number of values :"))

    for i in range(number):
        value.append(float(input("Enter the value :")))
        print(value)

        sumnum = sum(value)

    avgnum = sumnum/float(number)

    print("The average of the numbers is {}", avgnum)



if __name__ == '__main__':
    average()
