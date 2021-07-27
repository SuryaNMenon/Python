class Member:
  def __init__(self, name, age, pno, add, sal):
    self.name = name
    self.age = age
    self.pno = pno
    self.add = add
    self.sal = sal
  def printSalary(self):
    print(f"Salary of {self.name} is {self.sal}")
class Employee(Member):
  def __init__(self, name, age, pno, add, sal, spec):
        self.spec = spec
        Member.__init__(self, name, age, pno, add, sal)
  def printDetails(self):
        print(f"Name: {self.name}\nAge: {self.age}\nPhone Number: {self.pno}\nAddress: {self.add}\nSalary: {self.sal}\nSpecialisation: {self.spec}")
class Manager(Member):
  def __init__(self, name, age, pno, add, sal, dept):
    self.dept = dept
    Member.__init__(self, name, age, pno, add, sal)
  def printDetails(self):
        print(f"Name: {self.name}\nAge: {self.age}\nPhone Number: {self.pno}\nAddress: {self.add}\nSalary: {self.sal}\nDepartment: {self.dept}")

emp = Employee("Surya", 19, 7012288435, 8713, 50000, "Security")
man = Manager("Narayan", 34, 7012288435, 7413, 80000, "Consulting")

emp.printDetails()
emp.printSalary()

man.printDetails()
man.printSalary()
