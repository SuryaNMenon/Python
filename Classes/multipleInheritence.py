class Student:
  def __init__(self, name):
        self.name = name
  def readMarks(self, mark1, mark2, mark3):
    self.m1 = mark1
    self.m2 = mark2
    self.m3 = mark3
  def getMarks(self):
    print(f"Marks of {self.name} is:\nMark1: {self.m1}\nMark2: {self.m2}\nMark3: {self.m3}")
class Sports:
  def __init__(self, name):
    self.name = name
  def readSportMarks(self, smark):
    self.smark = smark
    print("Successfully read sports marks!")
  def getSportMarks(self):
    print(f"Sport marks of {self.name} is {self.smark}")
class totalMark(Student, Sports):
  def __init__(self, name):
        Student.__init__(self, name)
  def readMarks(self, mark1, mark2, mark3):
    self.m1 = mark1
    self.m2 = mark2
    self.m3 = mark3
    print(f"Successfully read Marks!")
  def getTotal(self):
    self.totalMark = self.m1 + self.m2 + self.m3 + self.smark
    print(f"Total marks of {self.name} is {self.totalMark}")

s1 = totalMark("Surya")
s1.readMarks(50, 100, 150)
s1.readSportMarks(200)
s1.getTotal()