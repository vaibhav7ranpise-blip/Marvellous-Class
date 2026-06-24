def main():
    print("Enter first no:")
    value1=int(input())

    print("Enter second no:")
    value2=int(input())

    ret = Addition(value1 , value2)  # ERROR - nameerror

    print("Addition is :", ret)

#stater
if __name__=="__main__":
    main()