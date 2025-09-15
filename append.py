a = [1, 2, 3, 4, 5]
a.append(6)
print(a)
b = int(input("Enter the element you want to remove: "))
a.remove(b)
print(a)

a = [2, 1, 8]
b = max([2, 1, 8])
c = min([2, 1, 8])
a.remove(b)
a.remove(c)
print("The second largest element: ",a)
