#Without Self
class Arithematic:
    def Add(No1,No2):
        Ans = No1 + No2
        return Ans

    def sub(No1,No2):
        Ans = No1 - No2
        return Ans
    
Aobj = Arithematic()

print("enter first number ")
Value1 = int(input())

print("enter second number ")
Value2 = int(input())

Ret = Aobj.Add(Value1,Value2)        #ERROR
print("Addition Is :",Ret)

Ret = Aobj.sub(Value1,Value2)       #ERROR
print("Substraction Is :",Ret)

"""
Output :
enter first number
11
enter second number
10
Traceback (most recent call last):
  File "C:\Users\HP\Desktop\Python\OOP_Python\objectOriented.py", line 18, in <module>
    Ret = Aobj.Add(Value1,Value2)
TypeError: Arithematic.Add() takes 2 positional arguments but 3 were given

>>>>>>Internaly called : Ret = Arithemetic.Add(Aobj,Value1,Value2) #

"""