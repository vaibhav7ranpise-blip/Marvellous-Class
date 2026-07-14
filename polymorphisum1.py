class Base:
    def fun(self):
        print("Inside base FUN")

class Derived(Base):
    def fun(self):
        print("Inside Derived FUN")


dobj = Derived()
dobj.fun()
