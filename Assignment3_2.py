def main():
        Data = []
        
        print("Enter number of elements : ")
        Size = int(input())

        print("Please enter numeric values : ")
        for i in range(Size):
            no = int(input())
            Data.append(no)

        print("Input data : ",Data)

        maximum = 0
        for i in Data:
            if i > maximum:
                maximum = i
        
        print("Maximum number is:",maximum)
             


if __name__=="__main__":
    main()