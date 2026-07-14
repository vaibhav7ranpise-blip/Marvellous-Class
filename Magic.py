class Demo:
    def __init__(self,A):
        self.No1 = A

obj1 = Demo(11)
obj2 = Demo(21)

print(obj1 + obj2)  #ERROR
"""PS C:\Users\HP\Desktop\Python\OOP-12July_2026\Polymorphisum> python .\Magic.py
Traceback (most recent call last):
  File "C:\Users\HP\Desktop\Python\OOP-12July_2026\Polymorphisum\Magic.py", line 8, in <module>
    print(obj1 + obj2)
          ~~~~~^~~~~~
TypeError: unsupported operand type(s) for +: 'Demo' and 'Demo'"""