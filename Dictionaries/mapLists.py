userlist1 = []
userlist2 = []
for iter in range(int(input("Enter the number of keys"))):
    userlist1.append(input("Enter key: "))
for iter in range(int(input("Enter the number of values"))):
    userlist2.append(input("Enter value: "))
userdict = dict(zip(userlist1,userlist2))
print(userdict)