
def Factorial(N):
    if N < 0:
        return print("Factorial is invalid")

    elif N==0:
        return 1

    else:
        X = 1   
        for i in range (1,N + 1):
            X = X*i
            
        return X
    
print("Enter your number")
No = int(input())

result = Factorial(No)

print("Factorial of", No , "is", result)