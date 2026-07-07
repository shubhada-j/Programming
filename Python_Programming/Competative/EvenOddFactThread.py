""" 
Design a Python application that creates two threads named EvenFactor and OddFactor.
Both threads should accept one integer number as a parameter.
The EvenFactor thread should:
Identify all even factors of the given number.
Calculate and display the sum of even factors.
The OddFactor thread should:
Identify all odd factors of the given number.
Calculate and display the sum of odd factors.
After both threads complete execution, the main thread should display the message:
"Exit from main"
"""

import threading

def EvenFact(No):
    Sum = 0

    for i in range(1,No+1):
        if (i % 2 == 0) and (No % i == 0):
            print("Even Factor : ",i)

            Sum = Sum + i

    print("Even Factors Sum is : ",Sum)

def OddFact(No):
    Sum = 0

    for i in range(1,No+1):
        if (i % 2 != 0) and (No % i == 0):
            print("Odd Factor : ",i)
            Sum = Sum + i
        
    print("Odd Factors Sum is : ",Sum)

def main():
    Value = int(input("Enter a number : "))
    t1 = threading.Thread(target=EvenFact, args=(Value,))
    t2 = threading.Thread(target=OddFact, args=(Value,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()