file = open("/Ghosty's Files/Programming/Python/Files/testfile.txt","r")
palinWordList = []
for line in file:
    line.strip("\n")
    line.strip(',')
    fileList = line.split()
    print(fileList)
    for iter in fileList:
        if len(iter) > 1 and iter == iter[::-1]: palinWordList.append(iter)
if len(palinWordList) == 0: print("No Palindrome words detected.")
else: print(f"List of Palindromes in the file is: {palinWordList}")
