'''
This code is for the study purpose the code is developed by
Rashid Imran Bilgrami, If you have any concerns please email me at
rashidbilgrami@hotmail.com or comments on GITHUB
'''

# Print Welcome Message
print("###### Welcome to Feet to Centimeter Converter Program ####")
# Getting input from the user, \n is using for new line
# cast in to float to make sure the input is number or the decimal
height = float(input("Enter Height in Feet::  \n"))


# Convert feet to cm
cm_value = height * 30.48

print("There are", cm_value, " in ", height, " ft")
