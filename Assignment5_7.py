def Area(Length,Width):

    total = (Length * Width)
    return total

def Perimeter(Length,Width):
    
    total = 2*(Length + Width)
    return total

print("Enter lenth of a rectangle")
a = int(input())

print("Enter width of a rectangle")
b = int(input())

print("Area of rectangle is:",Area(a,b))

print("Perimeter of rectangle is:",Perimeter(a,b))