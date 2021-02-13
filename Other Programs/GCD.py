#Program to compute gcd of two numbers.
num1 = 5538
num2 = 1105
gcd = 1
for i in range(1,num2+1):
    if(num1%i == 0 and num2%i == 0):
        if(i>gcd):
            gcd = i
print("The GCD of 5538 and 1105 is",gcd)
