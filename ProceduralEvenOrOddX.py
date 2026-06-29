def checkEven(No):
    if (No % 2 == 0):
        return True
    else:
        return False

def main():

    value = int(input("Enter Number :"))

    Ret = checkEven(value)

    if (Ret == True):
        print("Its Even Number")
    else:
        print("Its Odd NUmber ")


if __name__ == "__main__":
    main()