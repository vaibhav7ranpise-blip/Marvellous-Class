checkEven = lambda No:(No % 2 == 0)

def main():
    Data = [10,20,30,40,5,8]
    print("Input data is :",Data)

    FData = list(filter(checkEven,Data))

    print("Data After filter : ", FData)

if __name__ == "__main__":
    main()