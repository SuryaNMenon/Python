class Overload:
    def __init__(self, value):
        self.value = value
    def __truediv__(self,other):
        return self.value/other.value
p1 = Overload(5)
p2 = Overload(3)
print((p1/p2))