class Swap:
    def __init__(self,value):
        self.value = value
    def SwapNumber(self, other):
        temp = self.value
        self.value = other.value
        other.value = temp
    def printNumber(self):
        return self.value
p1 = Swap(5)
p2 = Swap(10)
print(f"Before swapping: {p1.printNumber()} {p2.printNumber()}")
Swap.SwapNumber(p1,p2)
print(f"After swapping: {p1.printNumber()} {p2.printNumber()}")