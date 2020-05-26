import math
'''
This code is for the study purpose the code is developed by
Rashid Imran Bilgrami, If you have any concerns please email me at
rashidbilgrami@hotmail.com or comments on GITHUB
'''

# Print Welcome Message
print("###### Welcome to Sum of n Positive Integers Program ####")
# Getting input from the user, \n is using for new line
# cast in to int to make sure the input is number
n = int(input("Enter value of n::  \n"))

# Calculate n number with the formula n * (n + 1)) / 2
sum_num = (n * (n + 1)) / 2

print("Sum of n Positive integers till ", n, " is %0.f" % sum_num)
