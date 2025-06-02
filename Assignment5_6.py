def CalculateTemp(Value):

    temp = (Value * 9/5) + 32

    return temp

print("Enter the temprature in celsius")
a = int(input())



fahrenheit = CalculateTemp(a)
print("Temperature in Fahrenheit is :", fahrenheit)