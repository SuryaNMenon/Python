file1 = open("/Ghosty's Files/Programming/Python/Files/testfile.txt","r")
file2 = open("/Ghosty's Files/Programming/Python/Files/testfile3.txt","a")
for line in file1:
    file2.write(line)
file2.write("\n")
file1.close()
file2.close()
file3 = open("/Ghosty's Files/Programming/Python/Files/testfile3.txt", "r")
for line in file3:
    print(line)