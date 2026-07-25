# Write a program that creates a text file after every minute

import time
import schedule
import datetime

def Create():
    timestamp = datetime.datetime.now()

    FileName = "File%s.txt"%(timestamp)
    FileName = FileName.replace(" ","_")
    FileName = FileName.replace(":","_")

    fobj  = open(FileName,"w")

    fobj.write(f"File name : {FileName}\n")
    fobj.write(f"Created at : {timestamp}\n")

    fobj.close()

    print("File created..\n")

def main():

    schedule.every(5).seconds.do(Create)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()