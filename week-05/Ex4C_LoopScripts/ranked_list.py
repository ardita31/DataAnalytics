# LAB 3

# Create a list of at least 5 items using anything you like: favorite foods, pets, cities you'd 
# like to visit, skills you want to develop, etc. Use enumerate() with a for loop to print each
# item as a numbered list, starting at 1. Now add an if statement inside your loop: if the index is 1 
# (i.e., the first item), also print "  <- top pick!" on the same line. 
# BONUS: Modify your loop to print the list in reverse order (still numbered 1 through 5) 
# using reversed() around your list. 

favorite = ['french fries', 'pizza', 'meat pie', 'tomatoes']
for i, food in enumerate(favorite, start=1): # enumerate gives you a number and item per loop for a list. You need two variables:
# i is the number, can be anything (index, number) and food is the name that holds one item at a time
# start=1 inside enumerate sets where counting begins
    if i == 1: # checks if we are on item number 1
        print(f'{i}. {food} <- top pick!')
    else:
        print(f'{i}. {food}')

# Output
# 1. french fries <- top pick!
# 2. pizza
# 3. meat pie
# 4. tomatoes

# Bonus: Reversed Rank
for i, food in enumerate(reversed(favorite), start=1):
    if i == 1: # checks if we are on item number 1
        print(f'{i}. {food} <- top pick!')
    else:
        print(f'{i}. {food}')

# Reveresed Output
# 1. tomatoes <- top pick!
# 2. meat pie
# 3. pizza
# 4. french fries