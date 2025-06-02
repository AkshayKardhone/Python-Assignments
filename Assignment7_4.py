from functools import reduce
#product = lambda no1,no2 : no1*no2

print("Enter number of elements")
size = int (input())

data = []
for i in range(size):
    a = int(input("Enter list elemets:   "))
    data.append(a)

print("Input list is: ",data)

RData = 0
RData = reduce(lambda no1,no2 : no1*no2 , data)

print("Product is: ",RData)