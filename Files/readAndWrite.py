with open("/Ghosty's Files/Programming/Python/Files/testfile4.txt","w+") as file:
    file.write(input("Enter the data to be entered into the file. EOL = NewLine"))
    file.seek(0)
    for line in file: print(line)