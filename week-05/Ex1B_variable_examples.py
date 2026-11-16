customer_id = 1001 # Customer IDs are typically stored as integers, if the ID contains letters, I would use string
customer_name = 'Will Smith' # Could also be written with separate variables
customer_gender = 'M' 
customer_dob = '12/14/2002' # Could need separate variables for month, day and year
drivers_license = '55896475'
auto_policy = '689745855'

my_name: 'Ardita Mrapshtija'
birth_city = 'Shkoder'
birth_country = 'Albania'

import keyword

print('Python Reserved Keywords:')
print()

for number, word in enumerate(keyword.kwlist, start=1):
    print(f'{number}. {word}')

print()
print(f'Total: {len(keyword.kwlist)} keywords')

# if: if runs a block of code only when a condition is True
# else: runs when the if condition is False. It never has its own condition.
# for: loops through a sequence (a list, a range, a string) and runs the indented code once per item.
# import: loads a module, a collection of ready-made code, so you can use its functions
# while: repeats a block of code as long as a condition stays true.


