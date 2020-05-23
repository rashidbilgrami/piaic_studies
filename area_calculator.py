'''
This code is for the study purpose the code is developed by 
Rashid Imran Bilgrami, If you have any concerns please email me at 
rashidbilgrami@hotmail.com or comments on GITHUB
'''
# Print Welcome Message
print("###### Welcome to Area Calculation Program ####")
# Getting input from the user, \n is using for new line
# cast in float because decimal value must be supported
circle_radius = float(input("Please Enter The Circle Radius: \n"))

# Area Formula is Area	= π r2 where pi value in math is 3.14
# Let make the r2 first
circle_radius *= circle_radius

# Getting area by multiply pi value with radious
area_value = 3.14159 * circle_radius

print("Great, The Area For Given Radius is: " + str(area_value))
