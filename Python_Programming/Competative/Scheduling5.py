# Write a script that schedules the following tasks:
# Print Lunch Time ! everyday at 1:00 PM
# Print Wrap up work every day at 6:00 PM

import time
import schedule

def Display():
    print("Lunch Time !")

def Show():
    print("Wrap up work")

def main():
    schedule.every().day.at("13:00").do(Display)
    schedule.every().day.at("18:00").do(Show)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()