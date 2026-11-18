# LAB 1 (continued using match/case)

dept_code = int(input('What is your department code: '))

match dept_code:
    case 1:
        print('Your department is Marketing!')
    case 5:
        print('Your department is Human Resources!')
    case 10:
        print('Your department is Accounting!')
    case 12:
        print('Your department is Legal!')
    case 18:
        print('Your department is IT!')
    case 20:
        print('Your department is Customer Relations!')
    case _:
        print('Invalid department code. Please re-enter: ')