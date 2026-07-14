class Base:
    def __init__(self):
        print("Inside base constructor")

#class  derived extends Base   Java
#class derived : public Base  C++

class derived(Base): #sengle inheritance
    def __init__(self):
        super().__init__()  #magic method call
        print("Inside Derived Constructore")

dobj = derived()