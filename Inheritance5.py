class Base:
    def __init__(self):
        print("Inside base constructor")

    def fun(self):
        print("inside Base FUn")

class derived(Base): #sengle inheritance
    def sun(self):
        print("inside derived SUN")

dobj = derived()
dobj.fun()
dobj.sun()