file1 = open("/Ghosty's Files/Programming/Python/Files/testfile.txt","r")
file2 = open("/Ghosty's Files/Programming/Python/Files/testfile2.txt","r")
file3 = open("/Ghosty's FIles/Programming/Python/Files/testfile3.txt","w")
for line in file1:
    file3.write(line)
file3.write("\n")
for line in file2:
    file3.write(line)
file3.close()
file4 = open("/Ghosty's Files/Programming/Python/Files/testfile3.txt","r")
for line in file4:
    print(line)