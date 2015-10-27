# while loops

i = 0
while i < 10:
    print(i)
    i += 1
# same as
for i in range(10):
    print(i)

i = 1
while i <= 2**32:
    print(i)
    i *= 2

# loop until user quits
'''quit = 'n'
while quit == 'n':
    quit = input('Do you want to quit? ')'''

# boolean to control while
done = False
while not done:
    quit = input('Do you want to quit? ')
    if quit == 'y':
        done = True
    attack = input('Does your elf attack the dragon?')
    if attack == 'y':
        print('Bad choice, you died.')
        done = True

# increment to end
value = 0.0
increment = 0.5
while value < 0.999:
    value += increment
    increment *= 0.5
    print(value)
