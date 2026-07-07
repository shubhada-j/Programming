"""
Write a program which contains filter(), map() and reduce() in it. 
Python application which contains one list of numbers. 
List contains the numbers which are accepted from user. 
Filter should filter out all such numbers which 
greater than or equal to 70 and less than or equal to 90. 
Map function will increase each number by 10. 
Reduce will return product of all that numbers.

Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70] 
List after filter = [76, 89, 86, 90, 701]
List after map = [86, 99, 96, 100, 80]
"""
from functools import reduce

CheckRange = lambda No : (No >= 70 and No <= 90)

IncreaseNum = lambda No : (No + 10)

Product = lambda No1, No2 : No1 * No2

def main():
    size = int(input("Enter number of elements: "))

    Data = []
    
    for i in range(size):
        Value = int(input("Enter number : "))
        Data.append(Value)

    FData = list(filter(CheckRange,Data))
    print("List after Filter = ",FData)

    MData = list(map(IncreaseNum,FData))
    print("List After Map : ",MData)

    RData = reduce(Product,MData)
    print("Product is : ",RData)

if __name__ == "__main__":
    main()