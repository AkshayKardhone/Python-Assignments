Square = lambda No : No * No
Cube = lambda No : No ** 3


a = int(input("Enter number: "))
ret = Square(a)
Ans = Cube(a)


print("Square is", ret)
print("Cube is", Ans)
