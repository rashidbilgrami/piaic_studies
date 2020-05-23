'''
This code is for the study purpose the code is developed by 
Rashid Imran Bilgrami, If you have any concerns please email me at 
rashidbilgrami@hotmail.com or comments on GITHUB
'''
# Print Welcome Message
print("###### Welcome to Divisibility Check of two numbers ####")
# Getting input from the user, \n is using for new line
# cast in float because may be the number value will be in decimal
numerator = float(input("Enter numerator or Top value: \n"))
denominator = float(input("Enter Denominator: or bottom value: \n"))


# Find Module the number
if (numerator % denominator == 0.00):
    print("Number " + str(numerator) +
          " is Completely divisible by " + str(denominator))
else:
    print("Number " + str(numerator) +
          " is not Completely divisible by " + str(denominator))
