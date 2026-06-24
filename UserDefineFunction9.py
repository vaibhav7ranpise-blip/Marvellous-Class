#Nested FUnction / Inner Function 
def BigBazar():
    print("Inside BIGBAZAR")

    def Amul():
        print("Inside AMUL ICE-CREAM Parlor")
    Amul()
    Amul()  

def main():
   BigBazar()   #Allowed
  
#stater
if __name__=="__main__":
    main()