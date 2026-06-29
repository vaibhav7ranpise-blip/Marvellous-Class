checkEven = lambda No :  (No % 2 == 0)

def main():

    value = int(input("Enter Number :"))

    Ret = checkEven(value)  #Ret = (Value % 2 == 0)

    if (Ret == True):
        print("Its Even Number")
    else:
        print("Its Odd NUmber ")


if __name__ == "__main__":
    main()