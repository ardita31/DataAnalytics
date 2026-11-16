# To calculate the tip amount we would need to multiply the subtotal of the bill with
#  what percentage we want to tip.
# Most typical tip % are 10%, 15%, 20% and if you feel generous 25%. 

# 1. Assign variables
subtotal = float(input('Enter subtotal: '))
tip_10 = .10
tip_15 = .15
tip_20 = .20
tip_25 = .25

# 2. Calculate 
tip_amount = subtotal * tip_20 # Lets say I want to tip 20%

# 3. Display
print(f'The tip on a ${subtotal} restaurant bill is ${tip_amount:.2f}')

# Output 
# Enter subtotal: 76.32
# The tip on a $76.32 restaurant bill is $15.26