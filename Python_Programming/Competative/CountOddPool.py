"""
Write a program that counts how many odd numbers exist between 1 and N.
Input Data [1000000, 2000000, 3000000, 4000000]
Expected Output Format
Process ID: 1237
Input Number: 1000000
Odd Number Count: 500000
"""
from multiprocessing import Pool
import os

def CountOdd(List):
    print(f"PID of CountOdd : {os.getpid()}")

    Count = 0

    for i in range(1,List+1):
        if i % 2 != 0:
            Count +=1

    return Count;   

def main():

    print(f"PID of Main : {os.getpid()}")

    Data = [1000000, 2000000, 3000000, 4000000]

    print("Input Data : ",Data)

    P = Pool()

    Result = P.map(CountOdd, Data)

    P.close()
    P.join()

    print("Odd numbers are : ",Result)

if __name__ == "__main__":
    main()