#Program to find simple interest using given values
p = int(input('Input the value of Principal'))
noDays = int(input('Input the value of number of days'))
rate = int(input('Input the value of rate of interest in terms of percentage'))
interest = rate*noDays*p/100;
print('Simple Interest =', interest)
