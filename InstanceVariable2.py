class Marvellous:
    #Class variable
    No1 = 11  #class Variable
    No2 = 12
    def __init__(self):
        #instance variable
        self.value1 = 21  #instance variable - 'self' is compalsory
        self.value2 = 51

print(Marvellous.No1)
print(Marvellous.No2)

#object/Instance creation
mobj1 = Marvellous()
mobj2 = Marvellous()
mobj3 = Marvellous()

print(mobj1.value1)
print(mobj2.value1)
