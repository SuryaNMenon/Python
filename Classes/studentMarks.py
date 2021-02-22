class Student:
    def readData(self):
        self.rollNo = int(input("Enter roll number of the student: "))
        self.mark1 = int(input("Enter their first mark: "))
        self.mark2 = int(input("Enter their second mark: "))
    def computeTotal(self):
        self.totalMarks = self.mark1 + self.mark2
    def printDetails(self):
        print(f"Mark 1 and Mark 2 of Roll number {self.rollNo} is {self.mark1} and {self.mark2} and the total mark is {self.totalMarks}.")
Student.readData()
