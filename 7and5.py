#Program to print numbers divisible by 7 and multiple of 5 in a user input range limit
lim=int(input('Enter the limit of the range'))
print('The numbers are ')
for i in range(0,lim+1):
    if(i%7==0 and i%5==0):
        print(i)
