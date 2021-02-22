from math import factorial
rowno = int(input("Enter the number of rows for Pascal's Triangle: "))
for i in range(rowno):
	for j in range(rowno-i+1):
		print(end=" ")
	for j in range(i+1):
		#nCr = n1//(n-r)! * r*
		print(factorial(i)//(factorial(i-j)*factorial(j)),end = " ")
	print()