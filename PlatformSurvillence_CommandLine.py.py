#python ProcessSurvillence.py 2 MarvellousLog
#pyhton ProcessSurvillence.py time_interval Folder_name
#           0
#len(sys.argv) -> 3


import psutil
import sys
import os

def main():
    Border = "-"*50
    print(Border)
    print("------Marvellous Platform Survellince System-----")
    print(Border)
    # -- h and  -- u handeler
    if(len(sys.argv ) == 2):
        if(sys.argv[1] == "--h"  or sys.argv[1] == "--H"):
            print("This Automation Script is USe to perform ")
            print("1 : It Fetch the info of running process")
            print("2 : It Fetch About the primary storage as RAM ")
            print("3 : It Fetch About the secondary storage as HDD ")
            print("4 : It Fetch About the Micro proceess ")
            print("5 : it maintain all records into log")
            print("6 : It get Out schedule periodically ")
            print("7 : It Send as log file thought the email")
            
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the Automation script as  :")
            print(f"python {sys.argv[0]} Time_Interval FOlder_Name")
            print("Time_Interval : Time is minuts for periodic execution ")
            print("FOlder_Name : Name of folder of ")
            
        else:
            print("Unable to procced as there is no matcing argument")
            print("Please use --h or -- u flag for getting more details")
            
    #Actual Project COde
    elif(len(sys.argv )== 3):
        pass
    else:
        print("Invalid no of argument")
        print("Unable to procced arguments not matching ")
        print("Please use --h or -- u flag for getting more details")
        
    
    print(Border)
    print("------Thank You for  Using our Automation System -----")
    print(Border)

if __name__ == "__main__":
    main()
    