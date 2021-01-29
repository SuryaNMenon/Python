#Program to print factorial of user input number
num = int(input('Enter the number\n'))
fact = 1
for iter in range(1,num+1):
    fact = fact * iter
print('Factorial of', num, 'is', fact)
