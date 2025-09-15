class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.set_marks(marks)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks if 0 <= marks <= 100 else 0

s = Student("v1z", 79)
print(s.get_name(), s.get_marks())
s.set_name("Bob")
s.set_marks(95)
print(s.get_name(), s.get_marks())
s.set_marks(120)
print(s.get_name(), s.get_marks())