'''
This code is for the study purpose the code is developed by
Rashid Imran Bilgrami, If you have any concerns please email me at
rashidbilgrami@hotmail.com or comments on GITHUB
'''


def dc_to_binary(num):
    if num > 1:
        dc_to_binary(num // 2)
    print(num % 2, end='')


# Print Welcome Message
print("###### Welcome to Decimal to Binary Program ####")
# Getting input from the user, \n is using for new line
# cast in to float to make sure the input is number
dc_number = int(input("Enter The Decimal Number::  \n"))


# Convert decimal to binary
dc_to_binary(dc_number)
