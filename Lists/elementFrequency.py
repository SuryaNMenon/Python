#Python program to find frequency of each element in user input list
userLis = [] 
lislen = int(input("Enter length of the list")) 
for iter in range(lislen): 
    elem = input("Enter the element") 
    userLis.append(elem) 
print(f"The input list is {userLis}") 
previousElem = None 
for currElem in userLis: 
    if previousElem == currElem: continue 
    else: flag = 0 
    for elemSearch in userLis: 
        if(elemSearch == currElem): 
            flag += 1 
    print(f"The element {currElem} appears {flag} times") 
    previousElem = currElem 
