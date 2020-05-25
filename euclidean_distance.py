import math
'''
This code is for the study purpose the code is developed by
Rashid Imran Bilgrami, If you have any concerns please email me at
rashidbilgrami@hotmail.com or comments on GITHUB
'''

# Print Welcome Message
print("###### Welcome to Euclidean distance Program ####")
# Getting input from the user, \n is using for new line
# cast in to int to make sure the input is number
x1 = int(input("Enter Co-ordinate for x1::  \n"))
x2 = int(input("Enter Co-ordinate for x2::  \n"))
y1 = int(input("Enter Co-ordinate for y1::  \n"))
y2 = int(input("Enter Co-ordinate for y2::  \n"))
x = (x1, x2)
y = (y1, y2)

# Find Distance
distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
print("Distance between points ", x, " and ", y, " is %.0f" % distance)
