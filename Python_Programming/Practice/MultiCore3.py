import time

def SumCube(No):
    Sum = 0
    
    for i in range(1,No+1):
        Sum = Sum + (i ** 3)        #i*i*i
    
    return Sum

def main():
    Data = [10000000,20000000,30000000,40000000,50000000]
    Result = []

    start_time = time.perf_counter()

    for value in Data:
        Ret = SumCube(value)
        Result.append(Ret)
    end_time = time.perf_counter()

    print("Result is :")
   
    print(Result)

    print(f"Time Required :{end_time-start_time:.4f}seconds")

    print("Result is :",Ret)
if __name__ == "__main__":
    main()

"""
Result is :
[2500000500000025000000000000, 40000004000000100000000000000, 202500013500000225000000000000, 640000032000000400000000000000, 1562500062500000625000000000000]
Time Required :8.7913
Result is : 1562500062500000625000000000000

"""

