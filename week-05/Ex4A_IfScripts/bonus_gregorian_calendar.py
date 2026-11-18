# BONUS LAB 
# Determine if a given year is a leap year 

# My first thought was to find a leap year depending on how many days February has. I had to see if Python 
# had a calendar module so I can start from there. 

import calendar

year = int(input('Enter a year: '))

feb_days = calendar.monthrange(year, 2)[1] 
# # monthrange() returns (start weekday, number of days) for February of the given year.
# [1] takes the second value (index 1), which is the number of days: 28 or 29.

if feb_days == 29:
    print(f'{year} is a leap year. February has {feb_days} days.')
else:
    print(f'{year} is not a leap year. February has {feb_days} days.')

# Output: 
# Enter a year: 2002
# 2002 is not a leap year. February has 28 days.