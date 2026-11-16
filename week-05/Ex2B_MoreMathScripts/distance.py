# The distance between two coordinates can be found using the euclidean distance formula,
# which is the square root of the sum of both differences in the x and y coordinates. 
# The official formula is d = √((x2 - x1)**2 + (y2 - y1)**2)

# 1. Assign values 
x1 = 7
x2= 4
y1= 5
y2= 9

# 2. Calculate 
from math import sqrt
distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Display the results
print(f'The distance between coordinates ({x1}, {y1}) and ({x2}, {y2}) is {distance}')
# The distance between coordinates (7, 5) and (4, 9) is 5.0
