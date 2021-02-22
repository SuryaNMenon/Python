def linearSearch(userlis, searchElem):
    flag = 0
    for  iter in range(len(userlis)):
        if userlis[iter] ==  searchElem: 
            print(f"Element  {searchElem} found at position {iter+1}")
            flag =1
    if flag == 0: print("Element not found")

userlis = []
for iter in range(int(input("Enter number of elements: "))):
    userlis.append(int(input("Enter an element: ")))
print("Entered list is",userlis)
linearSearch(userlis,int(input("Enter a value to be searched")))