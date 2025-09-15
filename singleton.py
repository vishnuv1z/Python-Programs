class Singleton:
    _instance=None       #instance is a variable and is initiated with none
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance
    
a=Singleton()
b=Singleton()
print(a is b)