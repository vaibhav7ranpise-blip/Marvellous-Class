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

        print(Demo.value1)
        print(Demo.value2)
    @classmethod        
    def gun(cls):
        print("INSIDE Class METHOD Gun")
    #print(Demo.No1)
    #print(Demo.No2)  not allowed

        print(Demo.value1)
        print(Demo.value2)

#Call without object
Demo.gun() 
