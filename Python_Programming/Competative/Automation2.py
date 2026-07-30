# Design Automation script which display information of running processes as its name, PID, Username

import sys
import os
import time
import psutil

def ProcessScan(ProccessName):
    listprocess = []

    for proc in psutil.process_iter():                                         #process_iter like walk
        info = proc.as_dict(attrs=["pid","name","username"])

        if(info["name"].lower() == ProccessName.lower()):
            listprocess.append(info)

    return listprocess

def Display(FolderName,ProcessName):
    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to procced as directory, name is existing but its not a directory")
            return

    else:
        os.mkdir(FolderName)                

        print("Directory fo the LogFile gets created Successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")                 

    FileName = os.path.join(FolderName,"Marvellous_%s.log"%timestamp) 

    try:
        fobj = open(FileName,"w")                                       
        print(f"Log File gets successfully created with name : {FileName}")

    except:
        print("Unable to create log file:")
        return

    Data = ProcessScan(ProcessName)

    if(len(Data) == 0):
        fobj.write("Process not found")

    else:
        for info in Data:
            fobj.write("-----------------------------------\n")
            fobj.write("PID : %s\n"%info.get("pid"))
            fobj.write("Name : %s\n"%info.get("name"))
            fobj.write("User Name : %s\n"%info.get("username"))

    fobj.close()

def main():
    if(len(sys.argv) != 3):
        print("Inavlid Number Of Arguments")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for getting more details")
        return
        
    if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
        print("This automation script is used to display")
        print("It fetch the information of running processes")


    elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
        print("Use the automation script as :")
        print(f"python {sys.argv[0]} Folder_Name Process_Name")
    else:  
        Display(sys.argv[1],sys.argv[2])      

if __name__ == "__main__":
    main()