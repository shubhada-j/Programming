# Write a lambda function using filter() which accepts a list of numbers and returns the product of all elements

from functools import reduce

Product = lambda No1, No2: (No1 * No2)

def main():
    size = int(input("Enter number of elements: "))

    Data = []
    
    for i in range(size):
        Value = int(input("Enter number : "))
        Data.append(Value)

    RData = reduce(Product,Data)

    print("Product of all numbers : ",RData)

if __name__ == "__main__":
    main()