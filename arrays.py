a = [10,20,30,40,50]
try:
    index = int(input("Enter an index: "))
    value = a[index]
    d = int(input("Enter a value: "))
    res = value/d
    print("Result : ",res)
except (ValueError, IndexError, ZeroDivisionError) as e:
    print(e)