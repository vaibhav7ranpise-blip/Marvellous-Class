class Demo:
    #class variables
    value1 = 10
    value2 = 20

    def __init__(self):
        self.No1 = 11
        self.No2 = 21

    #Instance method
    def fun(self):
        print("INSIDE INSTACE METHOD FUN")
        print(self.No1)
        print(self.No2)

        print(self.value1)
        print(self.value2)

dobj = Demo()
dobj.fun()
