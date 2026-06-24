def main():
    DATA = (10,20,30,40)

    print(type(DATA))
    print(len(DATA))

    print(DATA[0])
    print(DATA[1])
    print(DATA[2])
    print(DATA[3])

    DATA[1] = 21  #ERROR
    print(DATA[1])

if __name__ == "__main__":
    main()