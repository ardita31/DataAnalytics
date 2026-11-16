#The rule of 72 is a financial shortcut that estimates how long it will take for an 
# investment to double in value when earning an annual interest rate of return. To use 
# this rule, divide 72 by the annual interest rate (percentage) to get the approximate 
# years. 
# The official formula uses is t = 72 / R, 
# where t is the number of years to double and r is the annual interest rate in percent.
# Per rule of 72, interest rate should be a whole number. 

# 1. Assign variables
savings_balance = float(input('Enter the balance in your savings account: '))
interest_rate = 3

# 2. Calculations
time = int(72 / interest_rate)
doubled_value = savings_balance * 2

# 3. Display results 
print(f'Your current savings is ${savings_balance}')
# print(f'At a {interest_rate}% interest rate, your savings account will be worth ${doubled_value:.2f} in {time} years')
print(f'At a {format(interest_rate / 100, ".0%")} interest rate, your savings account will be worth ${format(doubled_value, ".2f")} in {format(time, ".1f")} years.')
# Output
# Your current savings is $456.0
# At a 3% interest rate, your savings account will be worth $912.00 in 24 years - other option
# At a 3% interest rate, your savings account will be worth $912.00 in 24.0 years.