""" 
Design a Python application that creates two threads named Prime and NonPrime.
Both threads should accept a list of integers.
The Prime thread should display all prime numbers from the list.
The NonPrime thread should display all non-prime numbers from the list.
"""

import threading

def Prime(List):
    for no in List:
        if no <= 1:
            continue
        
        for i in range(2,no):
            if(no % i == 0):
                break
        else:       
            print("Prime Number : ",no)

def NonPrime(List):
    for no in List:
        if no <= 1:
            continue
        
        for i in range(2,no):
            if(no % i == 0):
               print("Non-Prime Number : ",no)
               break

def main():
    size = int(input("Enter no. of elements : "))

    Data = []

    for i in range(size):
        Value = int(input("Enter a number : "))
        Data.append(Value)

    t1 = threading.Thread(target=Prime, args=(Data,))
    t2 = threading.Thread(target=NonPrime, args=(Data,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()