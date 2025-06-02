#Double = lambda No : No * 2

data = []
print("Enter number of elements")
size = int(input())

for i in range(size):
    a = int(input("Enter list element:  "))
    data.append(a)

print("Input list is: ",data)

MData = []

MData = list(map(lambda No : No * 2,data))
print("Doubled list ",MData)