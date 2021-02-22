with open("/Ghosty's Files/Programming/Python/Files/testfile4.txt","a") as file:
    file.write(input("Enter data to be inserted into the file. EOL = NewLine"))
with open("/Ghosty's Files/Programming/Python/Files/testfile4.txt", "r") as file:
    for line in file:
        print(line)