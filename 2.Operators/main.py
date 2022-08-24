#Problem 1
from math import pi
radius = float(input("Enter the radius of the circle: "))
def area(radius):
    return pi*radius*radius

print(area(radius))

#Problem 2
number = 5
def arithmetic(number):
    return number+number**2+number**3

print(arithmetic(number))

#Problem 3
date1 = [2014,7,2]
date2 = [2014,7,11]
def days(date1,date2):
    return abs(date2[-1]-date1[-1])

print(days(date1,date2))
