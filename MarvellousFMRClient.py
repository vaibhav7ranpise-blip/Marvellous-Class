
from MarvellousLibrary import filterX,mapX,reduceX

checkEven = lambda No:(No % 2 == 0)
Increamnet= lambda No:No + 1
Addition =  lambda No1,No2:No1 + No2

def main():
    Data = [10,20,30,40,5,8]
    print("Input data is :",Data)

    FData = list(filterX(checkEven,Data))

    print("Data After filter : ", FData)

    MData = list(mapX(Increamnet,FData))
    print("Mapped Data : ",MData)

    RData = reduceX(Addition,MData)
    print("Data After Reduce ",RData)

if __name__ == "__main__":
    main()