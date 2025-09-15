class Demo:
    def __enter__(self):
        print("Entering")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        print("Exiting...")
with Demo():
    print("Inside")

'''
with open("data.txt","r") as f:
    content=f.read()
#file automatically closes'''