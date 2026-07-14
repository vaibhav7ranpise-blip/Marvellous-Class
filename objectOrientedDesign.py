#Parameterise constructor
class Arithematic:  #incapsulation class
    def __init__(self,A,B):     #instance method - constructor
        self.No1 = A
        self.No2 = B

    def Add(self):          #instance method
        Ans = self.No1 + self.No2
        return Ans

    def sub(self):              #instance method
        Ans = self.No1 - self.No2
        return Ans
    



print("enter first number ")
Value1 = int(input())

print("enter second number ")
Value2 = int(input())

Aobj = Arithematic(Value1,Value2)  # Add parameter

#Ret = Add(Aobj,Value1,Value2) 
Ret = Aobj.Add()        #Remove paramter
print("Addition Is :",Ret)

Ret = Aobj.sub()       
print("Substraction Is :",Ret)
