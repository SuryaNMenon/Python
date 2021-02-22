rows = int(input("Enter number of rows of Floyde's Triangle: "))
value = 1
for i in range(1,rows+1):
    for j in range(1, i+1):
        print(value, end = " ")
        value = value+1
    print()