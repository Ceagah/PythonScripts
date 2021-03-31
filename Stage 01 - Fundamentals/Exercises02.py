# Create a script,that reads a float number, and show your int output

import math
num = float(input('Please, enter a float number ...'))
res = num.__floor__()

print(f'The floor number of {num} is {res}')


# Create a script that read the opposite side and adjacent side , and calc the hypotenuse
# the sum of the (two sides)pow 2 = hypotenuse

S1 = int(input('Please , enter the length of the opposite side: '))
S2 = int(input('Now please, enter the length of the adjacent side: '))

h = math.sqrt(S1.__pow__(2) + S2.__pow__(2)).__floor__()


print(f'The hypotenuse of {S1} and {S2} is {h}')

# Other way is using the ** operator

n1 = int(input('Please , enter the length of the opposite side : '))
n2 = int(input('Now please, enter the length of the adjacent side: '))

H = math.floor((n1**2 + n2**2)**(-2))
print(f'The hypotenuse of {n1} and {n2} is {H}')
