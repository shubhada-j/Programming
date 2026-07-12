#Write a program that calculates 1^5+2^5+3^5+.....+N^5 for multiple values of N simultaneously using Pool.
#Measure total execution time.

from multiprocessing import Pool
import time

def SumPower(List):
    Sum = 0

    for i in range(1,List+1):
        Sum = Sum + (i**5)
        
    return Sum
            

def main():
    
    size = int(input("Enter no. of elements : "))

    Data = []

    for i in range(size):
        Value = int(input("Enter a number : "))
        Data.append(Value)

    start_time = time.time()

    P = Pool()

    Result = P.map(SumPower, Data)

    P.close()
    P.join()

    print(" Sum is : ",Result)

    end_time = time.time()

    print(f"Time required : {end_time - start_time : .4f} seconds")

if __name__ == "__main__":
    main()