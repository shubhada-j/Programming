# Write a python program that monitors the size of a specified file every 30 seconds

import os
import time 
import schedule
import datetime

def Display(Data):
    if(os.path.exists(Data)):
        Size = os.path.getsize(Data)
        location = os.path.abspath(Data)
        print("Size of file is : ",Size, "bytes")

    else:
        print("File not exists")

    timestamp = datetime.datetime.now()

    fobj = open(Data,"a")
    fobj.write(f"Size of file is: {Size} bytes\n")
    fobj.write(f"Date and Time is : {timestamp}\n")
    fobj.write(f"Path of file is :{location}\n")

    fobj.close()

def main():
    File = input("Enter file name : ")

    schedule.every(30).seconds.do(Display,File)

    while True:
        schedule.run_pending()
        time.sleep(5)


if __name__ == "__main__":
    main()