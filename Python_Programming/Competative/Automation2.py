# Design Automation script which accept process name and display information of that process if it is running

import sys
import os
import time
import psutil


def ProcessScan(ProcessName):
    listprocess = []

    for proc in psutil.process_iter():
        
        info = proc.as_dict(attrs=["pid", "name", "username"])

        if info["name"].lower() == ProcessName.lower():
            listprocess.append(info)

    return listprocess


def Display(ProcessName):

    FolderName = "ProcessLog"

    if os.path.exists(FolderName):
        if not os.path.isdir(FolderName):
            print("Name exists but it is not a directory")
            return
    else:
        os.mkdir(FolderName)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Marvellous_%s.log" % timestamp)

    try:
        fobj = open(FileName, "w")

    except Exception as e:
        print("Unable to create log file:", e)
        return


    Data = ProcessScan(ProcessName)


    if len(Data) == 0:
        fobj.write("Process not found.\n")

    else:
        for info in Data:
            fobj.write("-----------------------------------\n")
            fobj.write("PID       : %s\n" % info.get("pid"))
            fobj.write("Name      : %s\n" % info.get("name"))
            fobj.write("User Name : %s\n" % info.get("username"))
            fobj.write("-----------------------------------\n")


    fobj.close()

    print("Log file created successfully :", FileName)

def main():

    if len(sys.argv) != 2:
        print("Invalid Number Of Arguments")
        print(f"Usage : python {sys.argv[0]} Process_Name")
        return


    if sys.argv[1] == "--h" or sys.argv[1] == "--H":
        print("This script accepts process name")
        print("and stores its information in log file")


    elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
        print("Usage :")
        print(f"python {sys.argv[0]} Process_Name")


    else:
        Display(sys.argv[1])


if __name__ == "__main__":
    main()