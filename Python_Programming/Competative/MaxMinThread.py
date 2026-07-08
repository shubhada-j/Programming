""" 
Design a Python application that creates two threads.
Thread 1st should calculate and display the maximum element from an list.
Thread 2nd should calculate and display the minimum element from the same list.
The list should be accepted from the user.
"""
import threading

def Maximum(List):
    Max = max(List)
    print("Maximum Element : ",Max)

def Minimum(List):
    Min = min(List)
    print("Minimum Element : ",Min)

def main():
    size = int(input("Enter no. of elements : "))

    Data = []

    for i in range(size):
        Value = int(input("Enter a number : "))
        Data.append(Value)

    t1 = threading.Thread(target=Maximum, args=(Data,))
    t2 = threading.Thread(target=Minimum, args=(Data,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()