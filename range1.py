#Program to display divisible numbers of 3 and 5 in user input range
low = int(input("Please enter the lower limit of the range"))
high = int(input("Please enter upper limit of the range"))
for i in range(low, high+1):
  if(i%3==0 and i%5==0):
    print(i,"\n")
