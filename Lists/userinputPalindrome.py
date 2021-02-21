#Python program to find whether a user input list is a palindrome 
lislen = int(input("Enter the length of the list")) 
userLis = [] 
for iter in range(lislen): 
    elem = input("Enter the element") 
    userLis.append(elem) 
list2 = userLis.copy() 
list2.reverse() 
if userLis == list2: 
    print("Palindrome") 
else: 
    print("Not Palindrome") 
