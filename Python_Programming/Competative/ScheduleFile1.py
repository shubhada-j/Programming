#Schedule a task that excutes every five minutes
#The task should write the current date and time into a file named : Marvellous.txt

import time
import schedule
import datetime

def Display():
    fobj = open("Marvellous.txt","a")
    
    fobj.write(f"Task Executed at : {datetime.datetime.now()}\n")

    fobj.close()

def main():
    schedule.every(5).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()