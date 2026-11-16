# There are X people going on a tour. Charter vans seat 15 passengers each. Vans cost
# $250 per day to rent (including the driver’s pay). How many vans do you need? How
# much will it cost to rent vans? What is the cost if you split it per person?

# 1. Assign variables
tourist_count = int(input('Enter number of tourists traveling: '))
vans_cost = 250

# 2. Calculate 
from math import ceil
vans_rented = ceil(tourist_count / 15)
total_cost = vans_rented * vans_cost
individual_cost = ceil(total_cost / tourist_count * 100) / 100
# If you multiply that out, how much did you collect?
 
# 3. Results
print(f'To accomodate {tourist_count} tourist you need {vans_rented} vans.')
print(f'Total cost of the vans is ${total_cost:,.2f}')
print(f'If split per person, individual cost will be ${individual_cost:,.2f}.')
print(f'Total money collected is ${(individual_cost * tourist_count):,.2f}')

# Enter number of tourists traveling: 38
# To accomodate 38 tourist you need 3 vans.
# Total cost of the vans is $750.00
# If split per person, individual cost will be $19.74.
# Total money collected is $750.12
# Why do you have leftover money? The extra 12 cents is the leftover from rounding everyone’s share up