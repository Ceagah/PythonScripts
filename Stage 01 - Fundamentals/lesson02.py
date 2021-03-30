# Primitive Type

# Sum of two numbers

n1 = int(input('Please, enter the first number ... '))
n2 = int(input('Now please, enter the second number ... '))
sum = n1 + n2
# print('The result is {}'.format(sum))
print(f'The result of the sum with {n1} and {n2} is {sum}')

# Discovering the type
# To descover the type of the input entry, just type before the variable, the term TYPE

n1 = input('Digit a character ... anyone...')
print(type(n1))

# Test if is numeric or is alpha
entry = input('Entry any character ...')
print(entry.isnumeric())
print(entry.isalpha())

#  Lesson 02 Challenges

# Sum of two number

n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))
sum = n1 + n2

print(f'The sum of {n1} and {n2} is {sum}')

# Read the input entry, and show all the information available

entry = input('Enter any character. .. ')
print(entry.isalpha())
print(entry.isnumeric())
print(type(entry))

