#-------------------------------------------------------------
#                           LIST        Tuple
#---------------------------------------------------------------
#Ordered                    Yes         Yes
#Indexed                    Yes         Yes
#Mutable                    Yes         NO    
#Hetrogenious               Yes         Yes
#---------------------------------------------------------------
def main():
   Data1 = [10,3.14,True,"PUNE"]   #List
   Data2 = (10,3.14,True,"PUNE")   #Tuple

   print(Data1)
   print(Data2)

   print(Data1[0])
   print(Data2[0])
if __name__ == "__main__":
    main()