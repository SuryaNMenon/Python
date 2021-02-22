file1 = open("/Ghosty's Files/Programming/Python/Files/testfile.txt","r")
file2 = open("/Ghosty's Files/Programming/Python/Files/testfile2.txt","r")
file3 = open("/Ghosty's Files/Programming/Python/Files/testfile5.txt","w+")
file1Content = file1.read()
file2Content = file2.read()
file3Content = file1Content + file2Content
file3.write(file3Content)
file3.close()
file4 = open("/Ghosty's Files/Programming/Python/Files/testfile5.txt","r")
for line in file4:
    print(line)