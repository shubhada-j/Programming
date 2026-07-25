# Write a program that reads and display the contents of a specified text file after every minute

import os
import time
import schedule
import datetime

def Display():
    try:
        if(os.path.exists("File.txt")):
            print("File exists")

            fobj = open("File.txt","r")

            Data = fobj.read()
            print(Data)

            fobj.close()
        
        elif(os.path.getsize("File.txt") == 0):
            print("File is empty")

    except PermissionError:
        print("Permission deined")

    except FileNotFoundError:
        print("File not found")   

def main():

    schedule.every(1).minute.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()