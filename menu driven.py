while True:
    print("\n-----CALCULATOR-----")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
    c = int(input("Enter an operation to perform : "))
    if(c == 5):
        print("Exiting the calculator...")
        break
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if(c == 1):
        print(a, " + ",b," = ",a+b)
    elif(c == 2):
        print(a, " - ",b," = ",a-b)
    elif(c == 3):
        print(a, " * ",b," = ",a*b)
    elif(c == 4):
        print(a, " / ",b," = ",a/b)
    else:
        print("Invalid choice.")