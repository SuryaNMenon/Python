#Program to reverse a given string.
str = input("Enter a string")
length = len(str)
newStr = ""
for i in range(length-1,-1,-1):
    newStr += str[i]
print(newStr)
