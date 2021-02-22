import os
with open("/Ghosty's Files/Programming/Python/Files/testfile3.txt","r") as file:
    print(f"The size of the file is",os.stat("/Ghosty's Files/Programming/Python/Files/testfile3.txt").st_size)
    file.seek(0,2)
    print(file.tell())