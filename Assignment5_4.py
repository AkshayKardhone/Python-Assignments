def Largrest(no1,no2,no3):
    if no1 >= no2 and  no1 >= no3:
        print(no1 ,"is greater")

    elif no2 >= no3 and no2 >= no1:
        print(no2, "Is greater")

    else:
        print(no3, "is greater")

a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))

Largrest(a,b,c)