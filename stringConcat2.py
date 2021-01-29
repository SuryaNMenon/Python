#Program to read 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
s1 = input("Enter a string\n")
s2 = input("Enter another string\n")
halflen = len(s1)//2
s3 = s1[:halflen]+s2+s1[halflen:]
print("The concatenated string is ", s3)
