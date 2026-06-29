def checkEven(No):
    return (No % 2 == 0)

def main():
    Data = [10,20,30,40,50,5,8]
    print("Input data is :",Data)

    FData = list(filter(checkEven,Data))

    print("Data After filter : ", FData)

   

if __name__ == "__main__":
    main()