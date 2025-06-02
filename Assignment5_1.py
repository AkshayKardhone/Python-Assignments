def Addition(value1,value2):
    ans = value1+value2
    return ans


def Substraction(value1,value2):
    ans = value1-value2
    return ans

def Multiplication(value1,value2):   
    ans = value1*value2
    return ans

def Division(value1,value2):    
    ans = value1/value2
    return ans


print("Enter first number")
no1 = int(input())
print("Enter second number")
no2 =  int(input())

print("Sum is:",Addition(no1,no2))

print("Difference is:",Substraction(no1,no2))

print("Product is:",Multiplication(no1,no2))

print("Division is:",Division(no1,no2))