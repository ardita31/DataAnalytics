# LAB 1 

# 1. Write a script named dept_converter.py that uses if/elif/else logic to determine
#and print department name based on a department code. Make sure to test your
#script with multiple codes.

dept_code = int(input('What is your department code: '))

if dept_code == 1:
    print('Your department is Marketing!')
elif dept_code == 5:
    print('Your department is Human Resources!')
elif dept_code == 10:
    print('Your department is Accounting!')
elif dept_code == 12:
    print('Your department is Legal!')
elif dept_code == 18:
    print('Your department is IT!')
elif dept_code == 20:
    print('Your department is Customer Relations!')
else:
    print('Invalid department code. Please re-enter: ')

