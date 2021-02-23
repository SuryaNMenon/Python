class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def Area(self):
        print(f"Area = {self.length * self.width}")
    def Perimeter(self):
        print(f"Perimeter = {2*(self.length + self.width)}")
rec1 = Rectangle(5,10)
rec2 = Rectangle(20,10)
rec1.Area()
rec2.Perimeter()