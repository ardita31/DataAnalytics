# The formula for temperature conversion from Celsius to 
# Fahrenheit is F = (9 / 5) * C + 32.

# 1. Assign variables
TempC = int(input('Enter temperature in Celcius: '))

# 2. Calculations
TempF = 9/5 * TempC + 32 # division and multiplication have the same precedence so no () are needed here

# 3. Display result
print(f'Temparature in Fahrenheit is {TempF:.1f}')
#Enter temperature in Celcius: 27
# Temperature in Fahrenheit is 80.6
