import cmath
def complexAdd(a, b):
    sum = a+b
    print(f"Sum of the two is: {sum}")
def complexSub(a,b):
    difference = a-b
    print(f"Difference between the two is {difference}")
def complexMult(a,b):
    product = a*b
    print(f"Product of the two is {product}")
a = complex(int(input("Enter real part of first number: ")), int(input("Enter imaginary part of first number: ")))
b = complex(int(input("Enter real part of second number: ")), int(input("Enter imaginary part of second number: ")))
print(f"Entered complex numbers are {a} and {b}")

complexAdd(a, b)
complexSub(a,b)
complexMult(a,b)