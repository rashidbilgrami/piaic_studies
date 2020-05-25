'''
This code is for the study purpose the code is developed by
Rashid Imran Bilgrami, If you have any concerns please email me at
rashidbilgrami@hotmail.com or comments on GITHUB
'''

# Print Welcome Message
print("###### Welcome to Triangle area Program ####")
# Getting input from the user, \n is using for new line
# cast in to float to make sure the input is number or the decimal
base = float(input("Enter magnitude of Triangle base::  \n"))
height = float(input("Enter magnitude of Triangle Hight::  \n"))


# find area of triangle b*h/2
area = (base*height)/2

print("Area of a Triangle with Height " + str(height) +
      " and Base  " + str(base) + "  is " + str(area))
