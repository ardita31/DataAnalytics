# Description: This script tests various numeric
# conversion techniques
# Author: Ardita Mrapshtija

a = " 101.1 "
b = '55' 
c = "402 Stevens" 
d = 'Number 5 ' 
# All the variables above are written as strings 
a = "  101.1 "

# 5a) Cast as integer using int()
# a_int = int(a) 
# Produces an error because int can only convert strings that are clean whole numbers. 
# It has decimals, and error message states it as an invalid literal for int()

# 5b) Cast as float using float()
a_float = float(a)
print(a_float, type(a_float))

# Output
# 101.1 <class 'float'>

# 5c) For variable a, try casting into a float then integer, like this: int(float(a))

a_int =  int(float(a))
print(a_int, type(a_int))

# Output
# 101 <class 'int'>

# 5d) Use slicing to add just the numeric portion of the string to a new variable
a_sliced = float(a[2:7])
print(a_sliced, type(a_sliced))

# Output
# 101.1 <class 'float'>

# 5e) Use the .strip() method for variables a and d to remove the leading/trailing spaces.
print(a.strip())

# Output
# 101.1

# Variable b 
b = '55'

# 5a) Cast as integer using int()
b_int = int(b) 
print(b_int, type(b_int))

# Output: 55 <class 'int'>

# 5b) Cast as float using float()
b_float = float(b)
print(b_float, type(b_float))

# Output
# 55.0 <class 'float'>

# 5d) Use slicing to add just the numeric portion of the string to a new variable
b_sliced = int(b[0:2])
print(b_sliced, type(b_sliced))

# Output
# 55 <class 'int'>

# 5e) .strip() method doesn't apply to variable b because it has no spaces.


# c = "402 Stevens" 

# 5a) Cast as integer using int()
# c_int = int(c) 
# Produces an error because int can only convert strings that are clean whole numbers. 
# It is not a number, and error message states it as an invalid literal for int()

# 5b) Cast as float using float()
# c_float = float(c)
# Produces as error because it is a string thats not a number. 
# Float cannot convert words to floats.

# 5d) Use slicing to add just the numeric portion of the string to a new variable
c_sliced = int(c[0:3])
print(c_sliced, type(c_sliced))

# Output
# 402 <class 'int'>

# 5e) .strip() method doesn't apply to variable c because it has no leading or trailing spaces.

# Variable d = 'Number 5  '

# 5a) Cast as integer using int()
# d_int = int(d) 
# Produces an error because int can only convert strings that are clean whole numbers. 
# Variable d has spaces, and error message states it as an invalid literal for int()

# 5b) Cast as float using float()
# d_float = float(d)
# Produces as error because it is a string thats not a number. 
# Float cannot convert words to floats.

# 5d) Use slicing to add just the numeric portion of the string to a new variable
d_sliced = int(d[7:8])
print(d_sliced, type(d_sliced))

# Output
# 5 <class 'int'>

# 5e) Use the .strip() method for variables a and d to remove the leading/trailing spaces.
print(d.strip())

# Output
# Number 5