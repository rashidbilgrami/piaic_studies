'''
This code is for the study purpose the code is developed by
Rashid Imran Bilgrami, If you have any concerns please email me at
rashidbilgrami@hotmail.com or comments on GITHUB
'''

# Print Welcome Message
print("###### Welcome to Calculate Interest Program ####")
# Getting input from the user, \n is using for new line
# cast in to float to make sure the input is number or the decimal
principle_amount = float(input("Please enter principal amount::  \n"))
intrest_amount = float(input("Please Enter Rate of interest in::  \n"))
years_required = int(input("Enter number of years for investment::  \n"))

# Calculate Intrest
total_amount = principle_amount * \
    (pow((1 + intrest_amount / 100), years_required))
total_interest = total_amount - principle_amount
print("Compound amount is %.2f" % total_amount)
print("Compound amount is %.2f" % total_interest)
