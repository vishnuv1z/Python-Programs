a = input("Enter the name: ")
try:
    mark = int(input("Enter the mark: "))
    if(mark < 0 or mark > 100):
        raise ValueError("mark should be > 0 and < 100")
except ValueError as e:
    print(e)