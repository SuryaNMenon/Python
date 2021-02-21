userdict = {}
for iter in range(int(input("Enter the number of key value pairs: "))):
	userdict[input("Enter a key: ")] = input("Enter a value: ")
print(userdict)
removeKey = input("Enter the key to be removed: ")
userdict.pop(removeKey)
print(userdict)