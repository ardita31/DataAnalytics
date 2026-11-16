# Federal taxes are 23% of your salary every month. How much is withheld for taxes?

# 1. Assign variables 
salary = float(input('Enter your salary: '))
federal_taxes = .23

# 2. Calculate
taxes_withheld = salary * federal_taxes

# 3. Display values 
print (f' Your total taxes withheld is ${taxes_withheld:,.2f}')
# Enter your salary: 75000
# Your total taxes withheld is $17,250.00