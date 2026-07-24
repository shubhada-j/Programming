#Write a python program that displays the current date and time after every one minute

import time
import schedule
import datetime


def Display():
    print("Current Date and ime is : " ,datetime.datetime.now())

def main():
    schedule.every(1).minute.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(5)

if __name__ == "__main__":
    main()