"""
Write a program that calculates factorials of multiple numbers simultaneously using Pool.map().
Display
-Process ID
-Input Number
-Factorial
"""

from multiprocessing import Pool
import os

def Factorial(List):
    print(f"PID of Factorial : {os.getpid()}")

    Fact = 1
    Sum = 0

    for i in range(1, List+1):
        Fact = Fact * i
        
    return Fact

def main():
    print(f"PID of Main : {os.getpid()}")

    size = int(input("Enter no. of elements : "))

    Data = []

    for i in range(size):
        Value = int(input("Enter a number : "))
        Data.append(Value)

    

    P = Pool()

    Result = P.map(Factorial, Data)

    P.close()
    P.join()

    print("Input Data : ",Data)

    print("Factorial is : ",Result)

if __name__ == "__main__":
    main()