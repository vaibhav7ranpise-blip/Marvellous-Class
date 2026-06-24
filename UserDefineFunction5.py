#Accept : Multiple Parameter
#Return : Multiple Value

def Marvellous(Value1,value2):
    print("Inside Marvellous :",Value1,value2)
    return 21,51,23

def main():
    ret1,ret2,ret3 = Marvellous(10,20)
    print("Return Values are :",ret1,ret2,ret3)
#stater
if __name__=="__main__":
    main()