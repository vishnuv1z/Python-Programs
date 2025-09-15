'''class Example:
    def __init__(self):
        self.name = "Vishnu"  #public variable

obj = Example()
print(obj.name)  #accessible
'''



'''class Example:
    def __init__(self):
        self._age=19   #protected variable

obj=Example()
print(obj._age)'''




'''class Example:
    def __init__(self):
        self.__salary=50000   #private variable

obj=Example()
print(obj.__salary)
print(obj._Example__salary)    #name mangling'''



class Employee:
    def __init__(self, name, salary):
        self.__name = name   #private variable
        self.__salary = salary    #private variable
    
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary
        

obj = Employee("La Pulga", 20000)
print(obj.get_name())
print(obj.get_salary())

obj.set_name("El Pistolero")
obj.set_salary(50000)

print(obj.get_name())
print(obj.get_salary())