"""
Write a program that accepts a list of integers and uses Pool.map() 
to calculate the sum of squares from 1 to N for every element in the list.
"""

from multiprocessing import Pool

def SumSquare(List):
    Sum = 0

    for i in range(1, List + 1):
        Sum = Sum + (i * i)

    return Sum

def main():
    size = int(input("Enter no. of elements : "))

    Data = []

    for i in range(size):
        Value = int(input("Enter a number : "))
        Data.append(Value)

    P = Pool()

    Result = P.map(SumSquare, Data)

    P.close()
    P.join()

    print("Sum is : ",Result)

if __name__ == "__main__":
    main()