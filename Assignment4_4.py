from functools import reduce

#CheckEven = lambda no : no % 2 == 0
    
#Square = lambda No : No * No
        
#Add = lambda No1,No2 : (No1 + No2) 


Data = []

print("Enter the number of Elements")
size = int(input())

print("Enter the numeric values")
for i in range(size):
    a = int(input())
    Data.append(a)

print("Input list is;", Data)

fData = []

fData = list(filter(lambda no : no % 2 == 0,Data))
print("List after filter is:",fData)

Mdata = []

Mdata = list(map(lambda No : No * No,fData))
print("List after Map is:", Mdata)

Rdata = 0
Rdata = reduce(lambda No1,No2 : (No1 + No2) ,Mdata)
print("Output of reduce is:",Rdata)

