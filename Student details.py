# ---------------------------------

# File          : Student details.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 27/04/2022
# Modified Date : 
# Description   : Sample program to use list for adding student details
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

if __name__ == '__main__':

    Student = ["Jacob"]

    Student.append(input("Enter the name of the student 1 : "))
    Student.append(input("Enter the name of the student 2 : "))
    Student.append(input("Enter the name of the student 3 : "))
    Student.append(input("Enter the name of the student 4 : "))
    Student.append(input("Enter the name of the student 5 : "))

    #print(Student)
    for x in Student:
        print(x)