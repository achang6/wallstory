# calculate miles per gallon
print('This program calculates mpg.')

# get miles driven from the user
miles_driven = input('Enter miles driven: ')
# convert text input to float
miles_driven = float(miles_driven)

# get gallons used from user
gallons_used = input('Enter gallons used: ')
# convert text input to float
gallons_used = float(gallons_used)

# calculate and print the answer
mpg = miles_driven / gallons_used
print('Miles per gallon: ', mpg)
