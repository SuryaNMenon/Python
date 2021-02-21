#Python program to remove punctuations from a user input sentence
userstr = input("Enter the sentence with atleast 2 punctuations")
strlist = list(userstr)
print(strlist)
punctlist = ['!',',','.',';',':','"',"'",'?',]
for punctuation in punctlist:
    if punctuation in strlist:
        strlist.remove(punctuation)
finalstr = ""
for iter in strlist:
    finalstr = finalstr + iter
print(finalstr)