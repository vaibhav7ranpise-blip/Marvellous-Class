Add = lambda No1,No2:No1 + No2
    
Sub = lambda No1,No2:No1 - No2

print("enter first number ")
Value1 = int(input())

print("enter second number ")
Value2 = int(input())

Ret = Add(Value1,Value2)
print("Addition Is :",Ret)
Ret = Sub(Value1,Value2)
print("Substraction Is :",Ret)
    