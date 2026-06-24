def BigBazar():
    print("Inside BIGBAZAR")

    def Amul():
        print("Inside AMUL ICE-CREAM Parlor")
def main():
   BigBazar()
   Amul()  #Error
   BigBazar.Amul() #Error
#stater
if __name__=="__main__":
    main()