from Marvellous import Addition ,Substraction 

def main():
    print("Enter first no:")
    value1=int(input())

    print("Enter second no:")
    value2=int(input())

    ret = Addition(value1 , value2) 
    print("Addition is :", ret)
    sub = Substraction(value1 , value2)
    print("Substraction is : ", sub)

#stater
if __name__=="__main__":
    main()