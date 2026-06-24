def Addition(NO1,NO2):   #global function
    ans = 0
    ans = NO1+NO2
    return ans

def main():
    print("Enter first no:")
    value1=int(input())

    print("Enter second no:")
    value2=int(input())

    ret = Addition(value1 , value2)

    print("Addition is :", ret)

#stater
if __name__=="__main__":
    main()