

from MarvellousNum import ChkPrime

def ListPrime():
    numbers = []
    total = 0

    print("Enter the number of the elements:")
    No = int(input())
    print("Enter the numbers:")
    for i in range(No):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)
    
    for i in numbers:
        if ChkPrime(i):
            total += i

    print(f"Sum of prime numbers: {total}")


ListPrime()
