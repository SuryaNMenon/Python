userdict1 = {}
userdict2 = {}
for iter in range(int(input("Enter the number of key value pairs of first dictionary"))):
    userdict1[input("Enter a key")] = input("Enter a value")
print(f"The first dictionary is {userdict1}")
for iter in range(int(input("Enter the number of key value pairs of second dictionary"))):
    userdict2[input("Enter a key")] = input("Enter a value")
print(f"The second dictionary is {userdict2}")
userdict2.update(userdict1)
print (userdict2)