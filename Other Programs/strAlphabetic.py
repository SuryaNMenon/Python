#Program to arrange string characters such that lowercase letters should come first. (string should contain both upper and lower case letters)
str = input("Enter a string\n")
alstr = ""
for i in str:
    if i.islower():
        alstr = alstr + i
for i in str:
    if i.isupper():
        alstr = alstr + i
print(alstr)
