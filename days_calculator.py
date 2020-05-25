from datetime import datetime
'''
This code is for the study purpose the code is developed by
Rashid Imran Bilgrami, If you have any concerns please email me at
rashidbilgrami@hotmail.com or comments on GITHUB
'''
# Print Welcome Message
print("###### Welcome to Days Calculator ####")
# Getting input from the user, \n is using for new line
# cast in date

start_date = datetime.strptime(
    input("Enter a start date in (dd/mm/yy) format:: \n"), '%d/%m/%Y')
end_date = datetime.strptime(
    input("Enter a start date in (dd/mm/yy) format:: \n"), '%d/%m/%Y')


# Find Date Difference Cast in dates to remove time span and days display only the days
print("There are " + str((datetime.date(end_date) - datetime.date(start_date)
                          ).days) + " day(s) in between (" + str(start_date.strftime('%d/%m/%Y')) + ") and (" + str(end_date.strftime('%d/%m/%Y')) + ")")
