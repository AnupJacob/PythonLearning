# ---------------------------------

# File          : classtest.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 28/04/2022
# Modified Date : 
# Description   : Sample program to check class functionality
# Licensing     : Anup Jacob, LYIT
# ----------------------------------


class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cars(Vehicle):
    def __init__(self):
        print("Engine Started")


if __name__=='__main__':
    car1 = Vehicle("BMW", "50000")

    print("Name of the car is "+car1.name)
    print("Price of the car is "+car1.price)
