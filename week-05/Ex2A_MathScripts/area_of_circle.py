# My birthday is December 14; the diameter for the circle will be 14. The formula for finding 
# the area of a circle is a = (pi * r**2) To find the radius of a circle from its diameter, 
#  divide the diameter by 2.

# 1. Assign variables
diameter = 14
radius = int(diameter / 2)

# 2. Calculations 
import math
area = math.pi * radius **2

# 3. Display results 
print(f'The area of a circle with radius {radius} is {area:.2f}')

# Output 
# The area of a circle with radius 7 is 153.94