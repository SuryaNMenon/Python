#Program to print sum of first N naturals where N is user input
N = int(input('Enter the limit of numbers\n'))
sum = 0
for iter in range(0,N,1):
    sum = sum + iter
print('Sum of first ', N, 'natural numbers is ', sum)
