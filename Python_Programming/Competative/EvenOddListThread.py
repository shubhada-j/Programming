""" 
Design a Python application that creates two threads named EvenList and OddList.
Both threads should accept a list of integers as input.
The EvenList thread should:
Extract all even elements from the list.
Calculate and display their sum.
The OddList thread should:
Extract all odd elements from the list.
Calculate and display their sum.
Threads should run concurrently.
"""

import threading

def EvenList(No):
    Sum = 0

    for Value in No:
        if (Value % 2 == 0):
            print("Even Number : ",Value)

            Sum = Sum + Value

    print("Even Sum is : ",Sum)

def OddList(No):
    Sum = 0

    for Value in No:
        if (Value % 2 != 0):
            print("Odd Number : ",Value)
            Sum = Sum + Value
        
    print("Odd Sum is : ",Sum)

def main():
    size = int(input("Enter no. of elements : "))

    Data = []

    for i in range(size):
        Value = int(input("Enter a number : "))
        Data.append(Value)
    
    t1 = threading.Thread(target=EvenList, args=(Data,))
    t2 = threading.Thread(target=OddList, args=(Data,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()