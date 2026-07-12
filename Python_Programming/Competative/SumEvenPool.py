"""
Write a Python program using multiprocessing. Pool to calculate the sum of all even numbers from 1 to N for every number from the given list.
Input Data [1000000, 2000000, 3000000, 4000000]
Expected Task
For each number N, calculate:
2+4+6 + N
Expected Output Format
Process ID: 1234
Input Number:1000000

"""

from multiprocessing import Pool
import os

def SumEven(List):
    print(f"PID of SumEven : {os.getpid()}")

    Sum = 0

    for i in range(1,List+1):
        if i % 2 == 0:
            Sum = Sum + i

    return Sum;   

def main():

    print(f"PID of Main : {os.getpid()}")

    Data = [1000000, 2000000, 3000000, 4000000]

    print("Input Data : ",Data)

    P = Pool()

    Result = P.map(SumEven, Data)

    P.close()
    P.join()

    print("Sum of Even numbers are : ",Result)

if __name__ == "__main__":
    main()