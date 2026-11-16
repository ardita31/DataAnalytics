# You are going to tile a room whose dimensions are length by width feet. There are
# twelve tiles per box, each 1 foot by 1 foot. How many boxes of tiles do you need? You
# can only buy full boxes, not a partial box.
# You also want to buy at least 10% more tiles than you need in order to handle chips,
# breakage, and mess-ups. How many total boxes will you buy?

# 1. Assign variables 
room_length = int(input('Enter room length (feet): '))
room_width = int(input('Enter room width (feet): '))
tile_size = 1 * 1

# 2. Calculations 
from math import ceil
room_area = room_length * room_width
count_tiles = (room_area / tile_size)
tile_boxes_needed = ceil(count_tiles / 12)
total_boxes_bought = (ceil(tile_boxes_needed * .10)) + tile_boxes_needed

# 3. Results
print(f'The room area is {room_area:.2f} sqaure feet, so you need {count_tiles} individual tiles.')
print(f'You need to buy {tile_boxes_needed} boxes to cover the area.')
print(f'To account for any mishaps you should buy {total_boxes_bought} boxes.')
# Enter room length (feet): 8
# Enter room width (feet): 10
# The room area is 80.00 sqaure feet, so you need 80.0 individual tiles.
# You need to buy 7 boxes to cover the area.
# To account for any mishaps you should buy 8 boxes.
