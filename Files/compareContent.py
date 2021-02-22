with open("/Ghosty's Files/Programming/Python/Files/testfile3.txt","r") as file1:
    with open("/Ghosty's Files/Programming/Python/Files/testfile2.txt","r") as file2:
        file1Content = file1.read()
        file2Content = file2.read()
        if file1Content == file2Content: print("Both files are same")
        else: print("Files are not same")