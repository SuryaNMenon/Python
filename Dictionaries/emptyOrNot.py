userdict = {}
for iter in range(int(input("Enter the number of key value pairs: "))):
    userdict[input("Enter key: ")] = input("Enter value: ")
print(userdict)
if len(userdict) == 0:
    print("Empty Dictionary")
else: print("Not empty")