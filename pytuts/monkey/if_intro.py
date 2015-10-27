# set up variables
a = 4
b = 5
c = 6

# basic comparisons
if a < b:
    print('a is less than b')
if a > b:
    print('a is greater than b')
if a <= b:
    print('a is less than or equal to b')
if a >= b:
    print('a is greater than or equal to b')
if a == b:
    print('a is equal to b')
if a != b:
    print('a is not equal to b')
# and
if a < b and a < c:
    print('a is less than b and c')
if a < b or a < c:
    print('a is less than either a or b or both')

# boolean
a = True
if a: 
    print('a is true')
if not a:
    print('a is false')

# can use boolean directly rather than comparison result
a = True
b = False
if a and b:
    print('a and b are both true')

# result of comparison is boolean
a = 3
b = 3
c = a == b
print(c)

# nonzero value is true
if 1:
    print('1')
if 'A':
    print('A')

# zero value is false
if 0:
    print('Zero')

a = 'c'
# wrong: will run regardless since 'b' is always true
if a == 'B' or 'b':
    print('a is equal to b. Maybe.')
# correct: will run only if either or both are true
if a =='B' or a == 'b':
    print('a is equal to b or B')

# examples

# if
temperature = int(input('What is the temperature in Fahrenheit? '))
if temperature > 90:
    print('It is hot outside')
print('Done')

# else
temperature = int(input('what is the temperature in Fahrenheit? '))
if temperature > 90:
    print('It is hot outside')
else:
    print('It is not hot outside')
print('Done')

# else if
temperature = int(input('What is the temperature in Fahrenheit? '))
if temperature > 90:
    print('It is hot outside')
elif temperature < 30:
    print('It is cold outside')
else:
    print('it is not hot or cold outside')
print('Done')


