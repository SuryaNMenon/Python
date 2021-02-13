#Program to find biggest of 3 numbers
a = int(input('Enter the first number'))
b = int(input('Enter the second number'))
c = int(input('Enter the third number'))
if(a>b and a>c):
  print(a, 'is the biggest number')
elif(b>a and b>c):
  print(b, 'is the biggest number')
else:
  print(c, 'is the biggest number')
