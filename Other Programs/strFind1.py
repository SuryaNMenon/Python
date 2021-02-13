#Program to find words with both alphabets and numbers
str = "COVID-19 : COVID19 affects different people in different ways. COVID19 infected people will develop mild to moderate illness"
count = 0
strList = str.split(" ")
for index in strList:
    if any(char.isalpha() for char in index) and any(digit.isnumeric() for digit in index):
        count += 1
print("Number of words is ",count)
