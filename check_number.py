'''
This code is for the study purpose the code is developed by 
Rashid Imran Bilgrami, If you have any concerns please email me at 
rashidbilgrami@hotmail.com or comments on GITHUB
'''
# Print Welcome Message
print("###### Welcome to Check Number either positive, negative or zero ####")
# Getting input from the user, \n is using for new line
# cast in float because may be the number value will be in decimal
user_number = float(input("Please Enter The Number: \n"))

# Check the number
if (user_number == 0.00):
    print("Zero Entered \n By You...")
elif (user_number < 0.00):
    print("Negative Number Entered \n By You...")
elif (user_number > 0.00):
    print("Positive Number Entered \n By You...")
else:
    print("I don't get your number \n By You...")
