class MyClass:
    name = "Vishnu"
    age = 19
obj1 = MyClass()
'''print(MyClass.name)
print(obj1.name)'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = 19

def stud_details(self):
    print(f"Hello my name is {self.name}")

'''obj1 = Person("Vishnu", 19) 
print(obj1.name)
print(obj1.age)'''

__str__ = "This is a custom string representation of the Person class."

#print(obj1)

def __str__(self):
    return f"Name: {self.name}, Age: {self.age}"

obj1 = Person("Vishnu", 19)
obj1.stud_details()
obj1.age = 20
print(obj1.age)

class Demo():
    pass