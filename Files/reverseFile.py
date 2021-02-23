file = open("/Ghosty's Files/Programming/Python/Files/testfile2.txt","r")
filelist = file.readlines()
for iter in reversed(filelist):
    print(iter)