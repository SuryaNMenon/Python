with open("/Ghosty's Files/Programming/Python/Files/testfile3.txt","r+") as file:
    fileContent = file.read()
    file.seek(0)
    file.write(fileContent.upper())
    file.seek(0)
    file.read()