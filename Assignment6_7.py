def find_largest(arr):
    
    
    largest = arr[0]
    
    for i in arr:
        if i > largest:
            largest = i
            
    print("Largest number is", largest)
          
    



n = int(input("How many elements? "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

print("Array:", arr)

find_largest(arr)


