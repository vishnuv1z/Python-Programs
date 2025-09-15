class animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(self.name, "speaks")  
class cat(animal):
    def meow(self):
        print(self.name, "Meow")
class dog(animal):
    def bark(self):
        print(self.name, "says bow bow")

a = animal("whiskers")
a.speak()
b = cat("Meownigga")
b.meow()
c = dog("Scooby doo")
c.bark()
c.speak()