class Demo:
    #class variables
    value1 = 10
    value2 = 20

    def __init__(self):
        self.No1 = 11
        self.No2 = 21

    
Dobj1 = Demo()
Dobj2 = Demo()      

Dobj1.No1 =0

print(Dobj1.No1)   #0
print(Dobj2.No1)   #11

#Dobj1.value1 = 0  #crete new variable by interpreter
Demo.value1 = 0    #access class variable

#print(Dobj1.value1)
#print(Dobj2.value2)

print(Demo.value1)