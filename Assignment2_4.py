def Sum(number):
    sum = 0
    for i in range (1,number):
        if number % i == 0:
            sum += i 
    return sum

print("Enter value")

No = int(input())


result = Sum(No)

print("The sum of factor of", No, "is", result)

