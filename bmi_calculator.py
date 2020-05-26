import math
'''
This code is for the study purpose the code is developed by
Rashid Imran Bilgrami, If you have any concerns please email me at
rashidbilgrami@hotmail.com or comments on GITHUB
'''

# Print Welcome Message
print("###### Welcome to BMI Calculator Program ####")
# Getting input from the user, \n is using for new line
# cast in to float to make sure the input is number or the decimal
height = float(input("Enter Height in Cm::  \n"))
weight = float(input("Enter Weight in Kg::  \n"))

# Calculate BMI BMI = weight (kg) / [height (m)]2
# convert height from cm to m
height = height/100
# round the answer with 2 decimal values
bmi = round(weight / (height**2), 2)

print("Your BMI is", bmi)
