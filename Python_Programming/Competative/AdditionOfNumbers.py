# Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements
from functools import reduce

Addition = lambda No1, No2 : (No1 + No2)

def main():
    size = int(input("Enter number of elements: "))

    Data = []
    
    for i in range(size):
        Value = int(input("Enter number : "))
        Data.append(Value)
        
    RData = reduce(Addition,Data)

    print("Addition is : ",RData)

if __name__ == "__main__":
    main()