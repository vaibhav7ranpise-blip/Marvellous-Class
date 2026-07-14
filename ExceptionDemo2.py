def main():
    Ans = 0
    try:
        print("Enter First number :") 
        No1 = int(input())

        print("Enter Second number :") 
        No2 = int(input())
        Ans =  No1 / No2

        print("Division is Succesfull")
        
    except ZeroDivisionError as Zobj:
        print("Exception Occured Deu to second oprand is Zero :",Zobj)
    print("Result is :", Ans)
    

if __name__ == "__main__":
    main()