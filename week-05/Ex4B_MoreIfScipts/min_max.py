a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))
c = int(input('Enter your third number: '))

if a > b > c:
    print(f'{a} is the largest number, {c} is the smallest number')
elif a > c > b: 
    print(f'{a} is the largest number, {b} is the smallest number')
elif b > a > c:
    print(f'{b} is the largest number, {c} is the smallest number')
elif b > c > a:
    print(f'{b} is the largest number, {a} is the smallest number')
elif c > a > b:
    print(f'{c} is the largest number, {b} is the smallest number')
elif c > b > a:
    print(f'{c} is the largest number, {a} is the smallest number')