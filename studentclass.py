class Student:
    def __init__(self, name, rollno, mark):
        self.name = name
        self.rollno = rollno
        self.mark = mark

a = Student("Vishnu", 29, 86)
b = Student("Rodxyll", 57, 92)
c = Student("v1z", 30, 68)

print("Name:", a.name)
print("Roll No:", a.rollno)
print("Mark:", a.mark)

print("\nName:", b.name)
print("Roll No:", b.rollno)
print("Mark:", b.mark)

print("\nName:", c.name)
print("Roll No:", c.rollno)
print("Mark:", c.mark)