class Demo:             #user define class
    #Constructor - always __init__()
    #districtore 
    def __init__(self):         #Constructor
        print("Inside COnstractor ")

    def __del__(self):          #distructor
        print("Inside Distructor")


obj1 = Demo()   #object create of class
obj2 = Demo()

print("End of Application ")