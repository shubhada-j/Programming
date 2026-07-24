# Write a program that scans a specified directory every minute

import os
import time
import schedule

def ScanDirectory(Data):
    if(os.path.exists(Data)):
        print("File Exists\n")
    
        for file in os.walk(Data):
            print(file,"\n")

    else:
        print("File not Exists")


def main():
    Value = input("Enter the path : ")

    schedule.every(1).minute.do(ScanDirectory,Value)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()