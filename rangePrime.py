#Program to print the prime numbers for a user provided range.
high = int(input("Enter the upper limit of the range"))
for i in range(1,high+1):
    flag=0
    for j in range(1,high+1):
        if(i%j==0):
            flag+=1
    if(flag==1 or flag==2):
        print(i)
