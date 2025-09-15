def sum(a):
    if(a==0):
        return 1
    else:
        return a+sum(a-1)
    
a=int(input("Enter the no: "))
print(sum(a))