def Patren(no):
    no+=1
    for i in range (no+1):
        for j in range (i,no-1):
                
            print("*", end="   ")
        print("\n")
    print()

a=int(input("Enter number "))
Patren(a)

