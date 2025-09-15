def count_up_to(n):
    for i in range(1, n+1):
        yield i       #To create number generator upto n numbers
for num in count_up_to(5):
    print(num)