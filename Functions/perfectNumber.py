def perfectNumber(x):
    divisorsum = 0
    for iter in range(x):
        if x%iter==0: divisorsum = divisorsum + iter;
    if divisorsum == x: print("Perfect number")
    else: print("Not perfect")

x = int(input("Enter number: "))
perfectNumber(x)