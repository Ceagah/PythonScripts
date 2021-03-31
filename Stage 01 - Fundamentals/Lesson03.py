# imports
# import math
# num = int(input('Enter a number '))

# square = math.sqrt(num)
# print(f'The SquareRoot of {num} is {square.__floor__()}')

# another way to import
from math import sqrt

num = int(input('Enter another number '))
square = sqrt(num)
print(f'The squareRoot of {num} is {square.__floor__()}')

# import external libs
import emoji
print(emoji.emojize("Hello World :earth_americas:", use_aliases=True))
