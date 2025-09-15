with open("filename.txt", "w") as file:
    file.write("Vishnu Hello")
    
with open("filename.txt", "r") as file:
    a = file.read()

i = a.split(" ")
print(i)
print(len(i))