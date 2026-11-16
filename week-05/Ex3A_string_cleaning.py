name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

# 3: Use .lower() to convert all three names to lowercase and print each result.

print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# Output
# priya sharma
# bob nguyen
# latonya williams

# 4: Use .title() to convert all three names to title case (first letter of each word capitalized), and print each result. 

print(name_1.title())
print(name_2.title())
print(name_3.title())

# Output
# Priya Sharma
# Bob Nguyen
# Latonya Williams

# 5: Use .replace() to remove the $ from both salary strings and print each result. 
# Add another print statement to test what data type these values are now.
# What would you need to do next to perform math on them?
print(salary_1.replace("$", ""))
print(salary_2.replace("$", ""))

# Output
# 82,500
# 74,000

# They are still strings because .replace() only modifies the string content, 
# it does not change the data type.
# To perform math on them, I would need to remove the comma and cast as int or float.

# 6: Chain .replace() and int() to produce a usable integer from salary_1
# Print the result and confirm its type using type()

salary_1_clean = int(salary_1.replace("$", "").replace(",", ""))
print(salary_1_clean, type(salary_1_clean))

# Output
# 82500 <class 'int'>