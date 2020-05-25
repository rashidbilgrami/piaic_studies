'''
This code is for the study purpose the code is developed by
Rashid Imran Bilgrami, If you have any concerns please email me at
rashidbilgrami@hotmail.com or comments on GITHUB
'''

# Print Welcome Message
print("###### Welcome to Vowel Tester Program ####")
# Getting input from the user, \n is using for new line
# cast in to str to make sure the input is number or the decimal
user_char = str(input("Enter Character::  \n")).lower()

# Predefined list for the vowels you can use tuple instead of list
vowels = ["a", "e", "i", "o", "u"]

# Boolean Variable to store value either system find the vowel or not
find_vowels = False

# Start finding Vowels
# Make sure user will not enter more than one character
if len(user_char) > 1:
    print("OOPS!!!! Sorry you can't allow to enter more than one character, Rerun the program and pass only one character like A or B or C")
elif len(user_char) == 1:
    # Match supplied character with the list items.
    for val in vowels:
        if str(val.lower()) == user_char:
            # In case of matching set the varibale true and break the loop
            find_vowels = True
            break
        else:
            pass

    # print the final result
    if find_vowels:
        print("Letter " + user_char.upper() + " is Vowel")
    else:
        print("Letter " + user_char.upper() + " is Not Vowel")

else:
    print("OOPS!!!! pass only one character like A or B or C")
