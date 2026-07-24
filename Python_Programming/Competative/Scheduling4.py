#Create a task that excutes every day at 9.00 AM and prints : "Namskar..."

import time 
import schedule

def Display():
    print("Namskar...")

def main():
    schedule.every().day.at("09:00").do(Display)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()