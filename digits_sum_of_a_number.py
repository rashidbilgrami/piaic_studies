import math
'''
This code is for the study purpose the code is developed by
Rashid Imran Bilgrami, If you have any concerns please email me at
rashidbilgrami@hotmail.com or comments on GITHUB
'''

# Print Welcome Message
print("###### Welcome to Digits Sum of a Number Program ####")
# Getting input from the user, \n is using for new line
# cast in to int to make sure the input is number
num = int(input("Enter a number::  \n"))
sum_num = 0
val = []
caption = ""
counter = 1
# Calculate sum
for i in str(num):
    sum_num += int(i)
    val.append(i)

for i in val:
    if counter == len(val):
        caption += str(i)
    else:
        caption += str(i) + " + "
        counter += 1

print("Sum of ", caption, " = ", sum_num)
