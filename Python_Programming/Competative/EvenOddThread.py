""" 
Design a Python application that creates two separate threads named Even and Odd.
The Even thread should display the first 10 even numbers.
The Odd thread should display the first 10 odd numbers.
Both threads should execute independently using the threading module.
Ensure proper thread creation and execution
"""

import threading

def EvenThread(No):
    for i in range(2,No+1,2):
        print(i)

def OddThread(No):
    for i in range(1,No,2):
        print(i)

def main():
    t1 = threading.Thread(target=EvenThread, args=(20,))
    t2 = threading.Thread(target=OddThread, args=(20,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()