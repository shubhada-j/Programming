import time
import multiprocessing
import os

def SumCube(No):
    print("Process is running with PID : ",os.getpid())
    Sum = 0
    
    for i in range(1,No+1):
        Sum = Sum + (i ** 3)        #i*i*i
    
    return Sum

def main():
    Data = [10000000,20000000,30000000,40000000,50000000]
    Result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()           #Pool-> taki

    Result = pobj.map(SumCube,Data)                     #this function is from pool class - differnet function but working same as map() function -> akavr jekam krt te saglyanvr krt

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Result is :")
   
    print(Result)

    print(f"Time Required :{end_time-start_time:.4f}seconds")

    
if __name__ == "__main__":
    main()



"""
Process is running with PID :  20064
Process is running with PID :  12320
Process is running with PID :  28064
Process is running with PID :  10096
Process is running with PID :  9828
Result is :
[2500000500000025000000000000, 40000004000000100000000000000, 202500013500000225000000000000, 640000032000000400000000000000, 1562500062500000625000000000000]
Time Required :6.4249seconds

"""