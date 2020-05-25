'''
This code is for the study purpose the code is developed by
Rashid Imran Bilgrami, If you have any concerns please email me at
rashidbilgrami@hotmail.com or comments on GITHUB
'''

# Print Welcome Message
print("###### Welcome to Check if number is Even or Odd Program ####")
# Getting input from the user, \n is using for new line
# cast in to int to make sure the input is number or the decimal
user_number = int(input("Enter Number::  \n"))

# Find reminder or module by dividing 2 even numbers are always return zero reminder if you divide the number by 2
if user_number % 2 == 0:
    print(str(user_number) + " is Even")
else:
    print(str(user_number) + " is Odd")
