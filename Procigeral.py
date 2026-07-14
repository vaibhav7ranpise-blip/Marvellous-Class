def Add(No1,No2):
    Ans = No1 + No2
    return Ans

def sub(No1,No2):
    Ans = No1 - No2
    return Ans

print("enter first number ")
Value1 = int(input())

print("enter second number ")
Value2 = int(input())

Ret = Add(Value1,Value2)
print("Addition Is :",Ret)

Ret = sub(Value1,Value2)
print("Substraction Is :",Ret)