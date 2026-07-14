#Multiple Inheritance
class Base1:
    
    def fun(self):
        print("inside Base1 FUn")

class Base2:

    def gun(self):
        print("inside Base2 Gun")

class derived(Base1,Base2): #sengle inheritance
    def sun(self):
        print("inside derived SUN")

dobj = derived()
dobj.fun()
dobj.gun()
dobj.sun()