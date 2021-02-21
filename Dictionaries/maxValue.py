userdict = {}
for iter in range(int(input("Enter the number of key value pairs: "))):
    userdict[input("Enter a key: ")] = input("Enter a value: ")
print(userdict)
maxvalue = max(userdict.values())
for k,v in userdict.items():
    if v == maxvalue: print("Max value is", v)
