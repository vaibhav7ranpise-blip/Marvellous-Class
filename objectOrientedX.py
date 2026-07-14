class Arithematic:
    def Add(self,No1,No2):
        Ans = No1 + No2
        return Ans

    def sub(self,No1,No2):
        Ans = No1 - No2
        return Ans
    
Aobj = Arithematic()

print("enter first number ")
Value1 = int(input())

print("enter second number ")
Value2 = int(input())

#Ret = Add(Aobj,Value1,Value2) 
Ret = Aobj.Add(Value1,Value2)        
print("Addition Is :",Ret)

Ret = Aobj.sub(Value1,Value2)       
print("Substraction Is :",Ret)
