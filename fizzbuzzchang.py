# fizz buzz challenge
# desperate submission

# rules
# for numbers 1 though 100
# print Fizz if divisible by 3
# print Buzz if divisible by 5
# print FizzBuzz if divisible by both (15)
# else print number

fishlist = range(1,101)

print fishlist

for fish in fishlist:
    if fish % 3 == 0:
        print 'Fizz'
        if fish % 5 == 0:
            print 'Buzz'
            print 'FizzBuzz'
    elif fish % 5 == 0:
        print 'Buzz'
    else:
        print fish

