def circArea():
    radius = int(input("Enter radius"))
    print("Area =", (3.14 * radius**2))
def triArea():
	base = int(input("Enter base"))
	height = int(input("Enter height"))
	print("Area =", (0.5 * base * height))
def recArea():
    length = int(input("Enter length"))
    breadth = int(input("Enter breadth"))
    print("Area =", length*breadth)
def squArea():
	side = int(input("Enter side"))
	print("Area=", (side*side))
while(1):
	choice = int(input("Menu\n1)Circle Area\n2)Triangle Area\n3)Rectangle Area\n4)Square area\nEnter your choice: "))
	if choice == 1: circArea()
	elif choice == 2: triArea()
	elif choice == 3: recArea()
	elif choice == 4: squArea()
	else: print("Wrong choice")