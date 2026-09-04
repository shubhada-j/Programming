import time
import threading

def SumEven(No):
    Sum = 0

    for i in range(2,No,2):
        Sum = Sum + i

    print("Summation of Even :",Sum)

def SumOdd(No):
    Sum = 0

    for i in range(1,No,2):
        Sum = Sum + i

    print("Summation of Odd :",Sum)

def main():
    start_time = time.perf_counter()

    t1 = threading.Thread(target=SumEven, args=(100000000,))
    t2 = threading.Thread(target=SumOdd, args=(100000000,))        
    
    t1.start()
    t2.start()

    end_time = time.perf_counter()

    print(f"Time require is : {end_time - start_time : .4f}")
if __name__ == "__main__":
    main()

"""
3 threads in the code -> main, SumEven, SumOdd

o/p:

Time require is :  0.0392
Summation of Odd : 2500000000000000
Summation of Even : 2499999950000000

"""