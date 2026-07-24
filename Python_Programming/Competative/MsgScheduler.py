# Write a program that schedules the message

import time
import schedule

def Display1():
    print("Start your weekly goals")
def Display2():
    print("Review your weekly progress")
def Display3():
    print("Weekly work completed")

def main():

    schedule.every().monday.at("09:00").do(Display1)
    schedule.every().wednesday.at("17:00").do(Display2)
    schedule.every().friday.at("18:00").do(Display3)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()


