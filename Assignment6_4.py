
def Factorial(N):
    count = 1
    for i in range(N,0,-1):
        count *= i
    return count
    
    
    
print("Enter your number")
No = int(input())

result = Factorial(No)

print("Factorial of", No , "is", result)