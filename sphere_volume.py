import math
'''
This code is for the study purpose the code is developed by
Rashid Imran Bilgrami, If you have any concerns please email me at
rashidbilgrami@hotmail.com or comments on GITHUB
'''
# my own function for truncate, you can use format or round but both change the value


'''
def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n
'''

# Print Welcome Message
print("###### Welcome to Calculate Volume of a sphere ####")
# Getting input from the user, \n is using for new line
# cast in float to make sure the input is number or the decimal

rad = float(input("Enter Radius of Sphere::  \n"))

# Find volume  by 4/3 * π * r3, the value of pi is 3.1415926535897931 predefined
vol = 4.0/3.0 * 3.1415926535897931 * rad ** 3
print("The Volume of Sphere is %.2f" % vol)
