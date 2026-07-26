#python ProcessSurvillence.py 2 MarvellousLog
#pyhton ProcessSurvillence.py time_interval Folder_name
#           0
#len(sys.argv) -> 3


import psutil
import sys
import os
import time
import schedule

def platformServillence(FolderName):   #Create folder
    Border = "-"*50
    Ret =  False  #folder check exist
    
    Ret = os.path.exists(FolderName) 
    
    if(Ret == True):
        Ret = os.path.isdir(FolderName)  # check folder is avilable
        if(Ret == False):   #folder sodun tya navachi file ahe
            print("Unable to procced ass folder name is existing but it is not a Directory")
            return    #go to main
    else:
        
        os.mkdir(FolderName)
        print("Directory for the log file created get successfully")
    
  ################################
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")  
    
    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)   #file entered in folder
    fobj = open(FileName,"w")
    print(f"Log file gets succesfully with name {FileName} ")
    
    fobj.write(Border+"\n")
    fobj.write("------Marvellous Platform Survellince System-----\n")
    fobj.write("LOgfile gets created at :"+timestamp+"\n")
    fobj.write(Border+"\n\n")
    
    fobj.write("------------System report----------------\n")
    fobj.write("Number of active cores  : %s\n" %psutil.cpu_count())
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")
    fobj.write("\n\n\n\n\n\n\n\n\n\n\n")
    
    fobj.write(Border+"\n")
    fobj.write("---------------End of log file----------------")
    fobj.write(Border+"\n")
    
    fobj.close()
        
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
        #print("CPU Usage :",psutil.cpu_percent())  
        print("Scheduler started SUccessfully")
        print("Press ctrl + c to abort the automation script")
        schedule.every(int(sys.argv[1])).minutes.do(platformServillence, sys.argv[2])
        while True:
            schedule.run_pending()
            time.sleep(1)
        
    else:
        print("Invalid no of argument")
        print("Unable to procced arguments not matching ")
        print("Please use --h or -- u flag for getting more details")
        
    
    print(Border)
    print("------Thank You for  Using our Automation System -----")
    print(Border)

if __name__ == "__main__":
    main()
    