# Assets that would need to be included in the calculation are anything of monetary value I own.
# This can include real estate property, cars, investments, or liquid money.
# Debts that need to be considered are any financial obligations someone owes. Liabilites can 
# include loans (car, mortage, personal, student) and any standard credit card debts or collections.



# 1. Determine the variables
checking_balance = float(input('Enter balance in checking account: '))
savings_balance = float(input('Enter balance in savings account: '))
cash = checking_balance + savings_balance
investments = float(input('Enter total investments: '))
student_loans = float(input('Enter total student loans: '))
cc_debt = float(input('Enter total credit card debt: '))

# 2. Calculate 
assets = cash + investments
liabilities = student_loans + cc_debt
net_worth = assets - liabilities

# 3. Display the results
print(f'Your total assets are ${assets:.2f}')
print(f'Your total debts are ${liabilities:.2f}')
print(f'Your net worth is ${net_worth:.2f}')

# Output
# Your total assets are $8463.96
# Your total debts are $9532.00
# Your net worth is $-1068.04