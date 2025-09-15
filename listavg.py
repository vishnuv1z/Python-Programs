a=list(map(int,input("Enter the elements: ").split(" ")))
avg=sum(a)/len(a)
for i in a:
    if (i>avg):
        print(i,end=" ")