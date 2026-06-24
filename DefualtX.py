def Area(Redius,PI=3.14,Redius): # ERROR - should be default the value in last 
    Ans = PI * Redius * Redius
    return Ans
def main():
    Ret = Area(10.5)
    print("Area  of Circle is :", Ret)

    Ret = Area(10.5,7.12)
    print("Area  of Circle is :", Ret)

if __name__ == "__main__":
    main()  