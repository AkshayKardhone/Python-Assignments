def main():
        Data = []
        
        print("Enter number of elements : ")
        Size = int(input())

        print("Please enter numeric values : ")
        for i in range(Size):
            no = int(input())
            Data.append(no)

        print("Input data : ",Data)

        minimum = Data[0]
        for i in Data:
            if i < minimum:
                minimum = i
        
        print("Minimum number is:",minimum)
             


if __name__=="__main__":
    main()