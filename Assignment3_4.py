def Frequency(Data,No):
    count = 0
    
    
    for i in Data:
        if No == i: 
            
            count =count+1
    
    return count


def main():
        Data = []
        
        print("Enter number of elements : ")
        Size = int(input())

        print("Please enter numeric values : ")
        for i in range(Size):
            no = int(input())
            Data.append(no)

        print("Input data : ",Data)
        print("Enter number to check")
        a = int(input())
        ans = Frequency(Data,a)
        print("Frequency is",ans)

        
           

if __name__=="__main__":
    main()