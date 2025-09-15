mark = int(input("Enter your mark: "))
if (mark <= 100 and mark >= 90):
    print("A1")
elif (mark < 90 and mark >= 80):
    print("A2")
elif (mark < 80 and mark >= 70):
    print("B1")
elif (mark < 70 and mark >= 60):
    print("B2")
elif (mark < 60 and mark >= 50):
    print("C1")
elif (mark < 50 and mark >= 40):
    print("C2")
elif (mark < 40 and mark >= 30):
    print("D")
elif (mark < 30 and mark >= 0):
    print("Fail")