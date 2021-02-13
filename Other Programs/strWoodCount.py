#Program to find number of occurances of the word wood
s = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
sList = s.split(" ")
count = 0
for i in sList:
    if i == 'wood':
        count += 1
print(count)
