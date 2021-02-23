class Operations:
    def __init__(self,value):
        self.value = value
    def __sub__(self, other):
        return self.value - other.value 

no1 = Operations(10)
no2 = Operations(15)
print(no1-no2)