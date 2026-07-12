"""
Write a Python program using multiprocessing. Pool to calculate the sum of all odd numbers from 1 to N.
Input
Data [1000000, 2000000, 3000000, 4000000]
Expected Task
For each number N, calculate:
1+3+5+ + N
Expected Output Format
Process ID: 1235
Input Number: 1000000
Sum of Odd Numbers 250000000000
"""


from multiprocessing import Pool
import os

def SumOdd(List):
    print(f"PID of SumOdd : {os.getpid()}")

    Sum = 0

    for i in range(1,List+1):
        if i % 2 != 0:
            Sum = Sum + i

    return Sum;   

def main():

    print(f"PID of Main : {os.getpid()}")

    Data = [1000000, 2000000, 3000000, 4000000]

    print("Input Data : ",Data)

    P = Pool()

    Result = P.map(SumOdd, Data)

    P.close()
    P.join()

    print("Sum of Odd numbers are : ",Result)

if __name__ == "__main__":
    main()