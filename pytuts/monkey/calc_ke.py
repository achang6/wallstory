# calculate kinetic energy

# welcome message
print('This program calculates the kinetic energy of a moving object.')

# receive mass
m_string = input('Enter the object\'s mass in kilograms: ')
# convert string input to float
m = float(m_string)

# receive velocity
v_string = input('Enter the object\'s velocity in m/s: ')
# convert string input to float
v = float(v_string)

# calculate KE, half mass times velocy squared
ke = 0.5 * m * v * v
print('The object has ' + str(ke) + ' joules of energy.')
