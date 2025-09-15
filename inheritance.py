class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def print_name(self):
        print(self.firstname, self.lastname)

x=Person("Alan", "Turing")
x.print_name()

class Student(Person):
    pass

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        super().__init__(fname, lname)
        self.graduation_year = 2028

y=Student("Vishnu", "Anup", 2028)
y.print_name()