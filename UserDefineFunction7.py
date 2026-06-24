#Accept : Multiple Parameter
#Return : Multiple Value
def Calculation(No1,No2):
    Mult= No1*No2
    Div = No1/No2

    return Mult,Div
    
def main():
   value1 = int(input("Enter First Number :"))
   value2 = int(input("Enter First Number :"))

   ret1,ret2 = Calculation(value1,value2)  

   print(" MULTIPLICATION IS :", ret1)
   print(" Division IS :", ret2)
#stater
if __name__=="__main__":
    main()