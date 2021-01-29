#Program to check if triangle with inputted values is equilateral or not
a = int(input("Please enter the first side"))
b = int(input("Please enter the second side"))
c = int(input("Please enter the third side"))
if(a==b and b==c and c==a):
  print("The triangle is equilateral")
else:
  print("The triangle is not equilateral")
