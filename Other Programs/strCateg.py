#Program to count all lower case, upper case, digits, and special symbols from a given string
UpperCase = 0
LowerCase = 0
Digits = 0
Special = 0
str = input("Enter a string")
for i in str:
    if i.isupper():
        UpperCase= UpperCase+1
    elif i.islower():
        LowerCase= LowerCase+1
    elif i.isalnum():
        Digits= Digits+1
    else:
        Special= Special+1
print("There are ", UpperCase," uppercase letters, ",LowerCase," lowercase letters, ",Digits," digits and ",Special," special symbols in ", str)
