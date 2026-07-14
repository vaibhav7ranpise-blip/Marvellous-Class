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

        print(cls.value1)  #Cls use against Demo as class methode
        print(cls.value2)
    @staticmethod  
    def sun():
        print("INSIDE Static METHOD name as SUN")
        print(Demo.value1)
        print(Demo.value2)

Demo.sun() #class variable access karu shakto pn karu naye

#Call with object
Dobj = Demo()
Dobj.gun() 
