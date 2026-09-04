import time
import threading

def SumEven(No):
    print("TID of SumEven thread is : ", threading.get_ident())
def SumOdd(No):
    print("TID of SumOdd thread is : ", threading.get_ident())

def main():
    print("TID of Main thread is : ", threading.get_ident())

    start_time = time.perf_counter()

    t1 = threading.Thread(target=SumEven, args=(100000000,))
    t2 = threading.Thread(target=SumOdd, args=(100000000,))        
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()

    print(f"Time require is : {end_time - start_time : .4f}")
if __name__ == "__main__":
    main()

"""
3 threads in the code -> main, SumEven, SumOdd

o/p:
TID of Main thread is :  20812
TID of SumEven thread is :  7228
TID of SumOdd thread is :  3156
Time require is :  0.0024
"""