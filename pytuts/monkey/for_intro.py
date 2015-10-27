# For loops

# print 'Hi' 10 times
for i in range(10):
    print('Hi')

# print 'Hello' 5 times and 'There' once
for i in range(5):
    print('Hello')
print('There')

# print 'Hello' 'There' 5 times
for i in range(5):
    print('Hello')
    print('There')

# print the numbers 0 to 9
for i in range(10):
    print(i)

# print the numbers from 1 to 10 (2 ways)
for i in range(1,11):
    print(i)
for i in range(10):
    print(i + 1)

# print even numbers from 2 to 10 (2 ways)
for i in range(2, 12, 2):
    print(i)
for i in range(5):
    print((i+1) * 2)

# count down from 10 to 1
for i in range(10, 0, -1):
    print(i)

# print numbers out of a list
for i in [2,6,4,2,4,6,7,4]:
    print(i)

# what does this print? why?
for i in range(3):
    print('a')
    for j in range(3):
        print('b')
# prints abbbabbbabbb, j for loop runs 3 times per i loop. 

# what is the value of a?
a = 0
for i in range(10):
    a += 1
print(a)
# 10

# what is the value of a?
a = 0
for i in range(10):
    a += 1
for j in range(10):
    a += 1
print(a)
# 20

# what is the value of a?
a = 0
for i in range(10):
    a += 1
    for j in range(10):
        a += 1
print(a)
# 100? oh forgot i loop. 110

# what is the value of sum?
sum = 0
for i in range(1,101):
    sum += 1
print(sum)
# 100?
