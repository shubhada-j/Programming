# Write a program that accepts : A message from the user and A time interval in seconds

import schedule
import time

def Display(Data):
    print(Data)

def main():
    msg = input("Enter Message : ")
    Time = int(input("Enter interval in seconds : "))

    schedule.every(Time).seconds.do(Display,msg)

    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()