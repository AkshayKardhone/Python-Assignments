from functools import reduce

Data = []

print("Enter the number of elements")
size = int(input())

print("Enter the numeric value")
for i in range(size):
    no = int(input())
    Data.append(no)


fData = []
filter_data = lambda no : no >= 70 and no <= 90

mData = []
Map_data = lambda No : No + 10

rData = 0    
Reduce_data = lambda No1,No2 : No1 * No2
    
    

print("Input list is:", Data)
fData = list(filter(filter_data,Data))
print("List after filter", fData)

mData = list(map(Map_data,fData))
print ("List after map",mData)

rData = reduce(Reduce_data,fData)
print("Output of reduce is:",rData)