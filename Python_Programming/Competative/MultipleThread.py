"""
Design a Python application where multiple threads update a shared variable.
Use a Lock to avoid race conditions.
Each thread should increment the shared counter multiple times.
Display the final value of the counter after all threads complete execution.
"""
import threading

Counter = 0                     #Shared Variable

LockObj = threading.Lock()      #Lock Object

def Increment():
    global Counter              

    for i in range(1000):
        LockObj.acquire()       #Acquire lock
        Counter = Counter + 1   #Critical Section
        LockObj.release()       #Release lock

def main():
    
    t1 = threading.Thread(target=Increment)
    t2 = threading.Thread(target=Increment)
    t3 = threading.Thread(target=Increment)
    t4 = threading.Thread(target=Increment)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("Final Counter Value :",Counter)

if __name__ == "__main__":
    main()