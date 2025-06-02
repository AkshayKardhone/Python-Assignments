#CheckEven = lambda No : No % 2 == 0

print("Enter number of elements")
size = int (input())

data = []
for i in range(size):
    a = int(input("Enter list elements; "))

    data.append(a)

print("input lis t is: ", data)

FData = []
FData = list(filter(lambda No : No % 2 == 0 , data))

print("Even numbers are: ", FData)



