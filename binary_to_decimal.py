'''
This code is for the study purpose the code is developed by
Rashid Imran Bilgrami, If you have any concerns please email me at
rashidbilgrami@hotmail.com or comments on GITHUB
'''


# Print Welcome Message
print("###### Welcome to Binary to Decimal Program ####")
# Getting input from the user, \n is using for new line
# cast in to float to make sure the input is number
binary_number = list(input("Enter The Binary Number::  \n"))
result = 0
caption = ""
# call decimal to binary
for i in range(len(binary_number)):
    single_digit = binary_number.pop()
    caption += str(single_digit)
    if int(single_digit) == 1:
        result += pow(2, i)

print("Decimal Representation of", caption, "is ",  result)
