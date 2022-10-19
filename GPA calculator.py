'''****************************************************************************************
# Author: Anup Jacob
# Version: 1.0
# Created date: 18/10/2022
# Modified date: 18/10/202
# Description: Program created to convert percentage to GPA and Vice versa2
****************************************************************************************'''

if __name__ == '__main__':
    print('Welcome to GPA to Percentage calculator')
    print('1. Percentage to GPA')
    print('2. GPA to Percentage')
    choice = int(input('\nEnter the conversion choice: '))

    if(choice == 1):
        percent = float(input('Enter the Percentage value: '))
        gpa = 4*percent/100

        print('\nThe GPA value of '+str(percent)+' is : '+str(gpa))
    elif(choice == 2):
        gpa = float(input('Enter the GPA value: '))
        percent = (gpa*100)/4

        print('\n The Percentage value of '+str(gpa)+' is '+str(percent))