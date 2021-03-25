print('Vai Carlão !')
# Print means console.log in Javascript


name = 'Carlos'
age = '27'
weight = '83'

print(name, age, weight)
# String concatenation ...

print('Hello , my name is ' + name + ' i am ' + age + ' years old, and i have ' + weight + ' kilos')
# String concatenation with set text ...


name = input('What is your name? ')
age = input('How old are you? ')

print('Hello '+ name + " ! . Nice to meet you ! You're a " + age + " years old! I'm 27. You do not ask, but i want to "
                                                                   "tell you")
# Input Strings ...

#  Lesson 01 Challenges
#  1 - write a script that read a input and give a welcome message

name = input('What is your name ? ')
print('Hello ' + name + '! Nice to meet you ! Did you see my github pages as well? Dont ? Access it ! '
                        'Is github.com/Ceagah')


# 2 - Script that read 3 inputs, day - month and year, and print it at DD/MM/YYYY

day = input('What the day, that you was born? ')
month = input('And the month ? ')
year = input('For last, the year, please ')

print("Thank you! Your born date is ...")

print(day + ' / ' + month + ' / ' + year)
