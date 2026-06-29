def checkEven(No):
    return (No % 2 == 0)

def Increamnet(No):
    return No + 1

def main():
    Data = [10,20,30,40,5,8]
    print("Input data is :",Data)

    FData = list(filter(checkEven,Data))

    print("Data After filter : ", FData)

    MData = list(map(Increamnet,FData))
    print("Mapped Data : ",MData)

if __name__ == "__main__":
    main()