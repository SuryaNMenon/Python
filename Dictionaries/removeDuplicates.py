userdict = {}
for iter in range(int(input("Enter the number of key value pairs: "))):
    userdict[input("Enter key: ")] = input("Enter value: ")
print(userdict)
duplist = []
resdict = dict()
for keys,values in userdict.items():
    if values in duplist: continue
    duplist.append(values)
    resdict[keys] = values;
print("Dictionary with removed duplicates is",resdict)