from functools import reduce

def Check_Prime(No):
    if No < 2:
        return False
    for i in range(2, int(No**0.5) + 1):
        if No % i == 0:
            return False
    return True
            
def Multiplication(No):
    Ans = No * 2
    return Ans 

def maximum(a,b):
    return a if a > b else b


data =[]

print("Enter the number of the elements")
size = int(input())

print("Enter the number")
for i in range (size):
    
    a = int(input())
    data.append(a)

print("Input list is :", data)

fData = []

fData = list(filter(Check_Prime , data))
print("List after filter is:",fData)

mData = []
mData = list(map(Multiplication,fData))
print("List after Map is:", mData)

rData = 0
rData = reduce(maximum , mData)
print("Output of reduce is:",rData)
