def Check_Prime(No):
    for i in range(2,No):
        if No % i == 0:
            print("Number is not prime")
            break
    else:
        print("Number is prime")


print("Enter a number") 
a = int(input())

Check_Prime(a)