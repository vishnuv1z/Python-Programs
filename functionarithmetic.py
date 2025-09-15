def add(a,b):
    c = a+b
    print(c)
def sub(a,b):
    c = a-b
    print(c)
def mul(a,b):
    c = a*b
    print(c)
def div(a,b):
    if(b==0):
        print("Division with 0 is not defined")
    else:
        c = a/b
        print(c)
I1 = int(input("Enter first value: "))
I2 = int(input("Enter second value: "))
add(I1,I2)
sub(I1,I2)
mul(I1,I2)
div(I1,I2)