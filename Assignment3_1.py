def main():
        Data = []
        
        print("Enter number of elements : ")
        Size = int(input())

        print("Please enter numeric values : ")
        for i in range(Size):
            no = int(input())
            Data.append(no)

        print("Input data : ",Data)

        sum = 0
        for i in (Data):
            sum += i

            

        print("Sum of input elements is:",sum)
    


if __name__=="__main__":
    main()