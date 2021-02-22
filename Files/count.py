file = open("/Ghosty's Files/Programming/Python/Files/testfile.txt","r")
lineCount = 0
wordCount = 0
charCount = 0
for line in file:
    line.strip("\n")
    wordlist = line.split()
    lineCount += 1
    wordCount = wordCount + len(wordlist)
    charCount = charCount + len(line)
print(lineCount, wordCount, charCount)
file.close()