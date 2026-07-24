# Write a program that created a new log file after every ten minutes

import time
import schedule
import datetime

def Create():
    timestamp = datetime.datetime.now()

    LogFileName = "Marvellous%s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    fobj  = open(LogFileName,"w")

def main():

    schedule.every(5).seconds.do(Create)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()