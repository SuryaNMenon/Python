#Program to print alphabetical pattern
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

fun = int(input("Enter no of the letter (1-26): "))

for i in range(fun):
    if (i > 0):
        print((i + 1) * alpha[i])
    else:
        print('A')
