# Lab 2 

# Assign variables 
pay_rate = float(input('Enter your pay rate: '))
hours_worked = eval(input('How many hours did you work: '))

# if statements 
if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
else: 
    gross_pay = pay_rate * hours_worked

print(f"{'Pay rate:':<19} ${pay_rate:.2f}")
print(f"{'Hours worked:':<19} {hours_worked}")
print(f"{'Gross pay:':<19} ${gross_pay:.2f}")

# Output 
# Enter your pay rate: 12.50
# How many hours did you work: 40
# Pay rate:           $12.50
# Hours worked:       40
# Gross pay:          $500.00


