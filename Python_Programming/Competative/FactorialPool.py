"""
Write a program that calculates factorials of multiple numbers simultaneously using multiprocessing.Pool.
Input
Data [10, 15, 20, 25]
Expected Task
For every N, calculate:N!
Expected Output Format
Process ID 1240
Input Number: 20
Factorial 2432902008176640000
"""

from multiprocessing import Pool
import os

def Factorial(List):
    print(f"PID of Factorial : {os.getpid()}")

    Fact = 1

    for i in range(1,List+1):
        Fact = Fact * i

    return Fact;   

def main():

    print(f"PID of Main : {os.getpid()}")

    Data = [10,15,20,25]

    print("Input Data : ",Data)

    P = Pool()

    Result = P.map(Factorial, Data)

    P.close()
    P.join()

    print("Factorial are : ",Result)

if __name__ == "__main__":
    main()