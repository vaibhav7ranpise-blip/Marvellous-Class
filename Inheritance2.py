class Base:
    def __init__(self):
        print("Inside base constructor")

#class  derived extends Base   Java
#class derived : public Base  C++

class derived: #sengle inheritance
    def __init__(self):
        print("Inside Derived Constructore")

    bobj = Base()