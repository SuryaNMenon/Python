#Program to find the roots of a quadratic equation
import cmath
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the third number"))
dis = (b**2) - (4 * a*c)
ans1 = (-b-cmath.sqrt(dis))/(2 * a)
ans2 = (-b + cmath.sqrt(dis))/(2 * a)
print('The roots are:')
print(ans1)
print(ans2)
