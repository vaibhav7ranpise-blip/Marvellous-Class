def checkEven(No):
    if (No % 2 == 0):
        print("It's EVEN number ")
    else:
        print("It's Odd Number ")

def main():

    value = int(input("Enter Number :"))

    checkEven(value)

if __name__ == "__main__":
    main()