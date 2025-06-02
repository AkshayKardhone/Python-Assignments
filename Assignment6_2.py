# Python program to calculate the sum of all the even numbers within the given range.

def main():

    
    sum = 0
    for i in range(0,101,2):
        if (i % 2 == 0):
            sum+=i
            
    print(sum)




if __name__=="__main__":
    main()