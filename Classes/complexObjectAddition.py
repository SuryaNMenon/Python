class Complex:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary
    def complexAddition(self, other):
        finalsum = Complex()
        finalsum.real = self.real + other.real
        finalsum.imaginary = self.imaginary + other.imaginary
        finalsum.printSum()
    def printSum(self):
        print(f"The sum of is {self.real}i+{self.imaginary}j")

p1 = Complex(5,7)
p2 = Complex(2,3)
Complex.complexAddition(p1,p2)
