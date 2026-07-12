"""
Write a program that counts how many even numbers exist between 1 and N using Pool.map().
Input
Data [1000000, 2000000, 3000000, 4000000]
Expected Output Format
Process ID: 1236
Input Number: 1000000
Even Number Count: 500000
"""

from multiprocessing import Pool
import os

def CountEven(List):
    print(f"PID of CountEven : {os.getpid()}")

    Count = 0

    for i in range(1,List+1):
        if i % 2 == 0:
            Count +=1

    return Count;   

def main():

    print(f"PID of Main : {os.getpid()}")

    Data = [1000000, 2000000, 3000000, 4000000]

    print("Input Data : ",Data)

    P = Pool()

    Result = P.map(CountEven, Data)

    P.close()
    P.join()

    print("Even numbers are : ",Result)

if __name__ == "__main__":
    main()