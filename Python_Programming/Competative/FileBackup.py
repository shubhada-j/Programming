# Write a program that performs a file backup every hour

import time
import schedule
import datetime

def FileBackup(First,Second):
    fobj1 = open(First,"r")
    Data = fobj1.read()
    timestamp = datetime.datetime.now()
    LogFileName = "%s_%s.log"%(Second,timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    fobj2  = open(LogFileName,"w")
    
    fobj2.write(Data)
    print("Data Copied")

    fobj2.close()
    fobj1.close()

def main():
    FName = input("Enter file name : ")
    SName = input("Enter file name : ")
    
    schedule.every(1).hour.do(FileBackup,FName,SName)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()