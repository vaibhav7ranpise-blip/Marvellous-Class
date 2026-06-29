from functools import reduce

def checkEven(No):
    return (No % 2 == 0)

def Increamnet(No):
    return No + 1

def Addition (No1,No2):
    return No1 + No2

def main():
    Data = [10,20,30,40,5,8]
    print("Input data is :",Data)

    FData = list(filter(checkEven,Data))

    print("Data After filter : ", FData)

    MData = list(map(Increamnet,FData))
    print("Mapped Data : ",MData)

    RData = reduce(Addition,MData)
    print("Data After Reduce ",RData)

if __name__ == "__main__":
    main()