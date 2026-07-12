#For every number in the given list, count how many prime numbers exist between 1 and N using multiprocessing Pool.
#Display total prime count for each number

from multiprocessing import Pool
import os

def PrimeNumber(List):
    if(List <= 1):
        return False

    for i in range(2, List):
        if(List % i == 0):
            return False
        
    return True

def CountPrime(no):
    Count = 0

    for i in range(1,no+1):
        if(PrimeNumber(i)):
            Count = Count + 1

    return Count
            

def main():
    
    size = int(input("Enter no. of elements : "))

    Data = []

    for i in range(size):
        Value = int(input("Enter a number : "))
        Data.append(Value)

    P = Pool()

    Result = P.map(CountPrime, Data)

    P.close()
    P.join()

    print("Prime number are : ",Result)

if __name__ == "__main__":
    main()