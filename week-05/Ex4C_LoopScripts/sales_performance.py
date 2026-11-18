# LAB 4

# You have been given the following list of sales records. Each record is a tuple 
# containing a salesperson's name, their region, and their total sales for the month: 
# Use a for loop to unpack each tuple directly in the loop statement, and print a 
# summary line for each record that looks like this: 
# Marcus Webb (East): $4,250.00 
# Priya Sharma (West): $5,875.50 
# Add a conditional inside your loop: if a salesperson's total is greater than $5,000, also 
# print "  ^ Top performer!" below their summary line. 
# BONUS: Add a variable before the loop to track total sales across all employees, and 
# print the overall total after the loop finishes. 

sales_data = [
('Marcus Webb', 'East', 4250.00),
('Priya Sharma', 'West', 5875.50),
('DeShawn Carter', 'East', 3100.75),
('LaTonya Rivers', 'South', 6420.00),
('Bob Nguyen', 'West', 4980.25),
]

print('Sales Performance Report')
print('-' * len('Sales Performance Report'))

total_sales = 0

for name, region, sales in sales_data:
    print(f'{name}, ({region}): ${sales:,.2f}')
    if sales > 5000:
        print(' ^ Top performer!')

total_sales += sales

print(f'\nTotal sales across all employees: ${total_sales:,.2f}')

# Output 
# Sales Performance Report
# ------------------------
# Marcus Webb, (East): $4,250.00
# Priya Sharma, (West): $5,875.50
# ^ Top performer!
# DeShawn Carter, (East): $3,100.75
# LaTonya Rivers, (South): $6,420.00
#  ^ Top performer!
# Bob Nguyen, (West): $4,980.25

# Total sales across all employees: $4,980.25
