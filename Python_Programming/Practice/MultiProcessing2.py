import os
import time
import multiprocessing

def SumEven(No):
    print(f"PID of SumEven : {os.getpid()} PPID of SumEven : {os.getppid()}")
   
    Sum = 0

    for i in range(2,No,2):
        Sum = Sum + i

    print("Summation of Even :",Sum)

def SumOdd(No):
    print(f"PID of SumOdd : {os.getpid()} PPID of SumOdd : {os.getppid()}")

    Sum = 0

    for i in range(1,No,2):
        Sum = Sum + i

    print("Summation of Odd :",Sum)

def main():
    print(f"PID of Main : {os.getpid()} PPID of Main : {os.getppid()}")

    start_time = time.perf_counter()

    t1 = multiprocessing.Process(target=SumEven, args=(100,))
    t2 = multiprocessing.Process(target=SumOdd, args=(100,))        
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()

    print(f"Time require is : {end_time - start_time : .4f}")
if __name__ == "__main__":
    main()

"""
PID of Main : 23820 PPID of Main : 9140
PID of SumEven : 18060 PPID of SumEven : 23820
Summation of Even : 2450
PID of SumOdd : 18308 PPID of SumOdd : 23820
Summation of Odd : 2500
Time require is :  0.074241

"""