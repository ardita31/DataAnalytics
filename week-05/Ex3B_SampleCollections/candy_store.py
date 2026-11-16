# Question 2: Start by creating two tuples: one that lists at least 3 
# types of candy that can come in fruit flavors, and another that lists
# at least 3 fruity flavors. 

candy_types = ("Skittles", "Twizzlers", "Nerds")
candy_flavors = ("Strawberry", "Lemon Lime", "Apple")

# Question 3: Now create a new variable to store candy combinations as a set. 
# Using the index of each tuple, add at least one combination of each candy and 
# flavor to the new set. For example, putting together tuple1[0] and tuple2[1] 

candy_combinations = set()

candy_combinations.add(candy_types[0] + " with " + candy_flavors[1])
candy_combinations.add(candy_types[1] + " with " + candy_flavors[0])
candy_combinations.add(candy_types[2] + " with " + candy_flavors[2])

# Question 4: Create an output message that says, “Today’s candy options include:” and 
# then prints the contents of the set. 

print("Today's candy options include:")
print(candy_combinations)

# Output
# Today's candy options include:
{'Nerds with Apple', 'Twizzlers with Strawberry', 'Skittles with Lemon Lime'}

# Question 5: Print the output multiple times. What do you notice about the order of the 
# items as you repeat the output?

print("Today's candy options include:")
print(candy_combinations)
print("Today's candy options include:")
print(candy_combinations)

# Output
# Today's candy options include:
# {'Twizzlers with Strawberry', 'Skittles with Lemon Lime', 'Nerds with Apple'}
# Today's candy options include:
# {'Twizzlers with Strawberry', 'Skittles with Lemon Lime', 'Nerds with Apple'}
# Today's candy options include:
# {'Twizzlers with Strawberry', 'Skittles with Lemon Lime', 'Nerds with Apple'}

# As I repeated the output, the order of items in the set remained the same throughout.
