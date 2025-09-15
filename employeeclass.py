class Employee:
    count = 0
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.count += 1

    def EmpDetails(self):
        print("\nName   : ",self.name)
        print("Age    : ",self.age)
        print("Salary : ",self.salary)

e1 = Employee("Suresh", 36, 30000)
e2 = Employee("Rajesh", 31, 28000)
e3 = Employee("Niggesh", 69, 42000)

e1.EmpDetails()
e2.EmpDetails()
e3.EmpDetails()

print("Total number of employees :", Employee.count)