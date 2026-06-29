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