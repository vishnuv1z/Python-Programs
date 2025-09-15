flag=0
num = int(input("Enter a number: "))
for i in range(2, num):
    if (num % i==0):
        flag = 1
        break
if (flag == 0):
    print("It is a prime number")
else:
    print("It is not a prime number")
