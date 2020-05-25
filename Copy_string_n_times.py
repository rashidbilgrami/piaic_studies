'''
This code is for the study purpose the code is developed by
Rashid Imran Bilgrami, If you have any concerns please email me at
rashidbilgrami@hotmail.com or comments on GITHUB
'''

# Print Welcome Message
print("###### Welcome to Copy string n times ####")
# Getting input from the user, \n is using for new line
user_word = input("Enter String::  \n")

# cast in to int to make sure the input is number or the decimal
loop_value = int(input("How many copies of String you need::  \n"))

# looping the user input, you can use while loop also to achieve this task
for i in range(loop_value):
    print(user_word)
