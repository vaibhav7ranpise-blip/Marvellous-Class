# self create filter , map reduce
checkEven = lambda No:(No % 2 == 0)
Increamnet= lambda No:No + 1
Addition =  lambda No1,No2:No1 + No2

def filterX(task,elements):
    result = []         #list[]

    for no in elements:
        ret = task(no)  #checkEven(no)

        if(ret == True):
            result.append(no)
    return result

def mapX(task,elements):
    result = []

    for no in elements:
        ret = task(no)      #increamenet(no)
        result.append(ret)
    return result

def reduceX(task,elements):             #self created
    sum = 0
    for no in elements:
        sum = task(sum,no)
    return sum

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